# CyberTalents - Fisherman CTF Writeup

**Category:** Digital Forensics  
**Difficulty:** Medium  
**Platform:** CyberTalents  

---

## Overview
**Fisherman** is a digital forensics challenge where we are presented with a memory dump (`mem.tar.7z`) extracted from a compromised mobile device belonging to a victim named Jack, who suddenly lost all his savings in a phishing/lottery scam. Our objective is to analyze the memory dump, trace the malicious phishing artifacts, and uncover the hidden flag.

---

## Step-by-Step Solution

### Step 1: Extracting and Preparing the Memory Dump
First, we downloaded the challenge archive file (`mem.tar.7z`) and extracted its contents using the archive utilities and `tar` command to retrieve the raw memory dump file (`mem`).

```bash
7z x mem.tar.7z
tar -xvf mem.tar
```

*Result:* We successfully obtained the raw memory dump file named `mem` ready for string and forensic analysis.

![Extracting Memory Dump](image_9af0a8.png)

---

### Step 2: Searching for Strings and Artifacts
Since the challenge description hinted at a phishing scenario involving Facebook and a fake bank lottery scheme, we used the `strings` command combined with `grep` to look for relevant keywords and URLs within the memory image:

```bash
strings mem | grep -i "facebook"
```

*Result:* The search revealed multiple references to a local phishing URL and SMS templates related to a fake bank lottery campaign:
```text
http://192.168.1.2/bank%20lottery/?facebook/this_is_mr_jack_fb_account
by default the sms is base64 encoded, but the flag is (base64 encoded * 2) and xored with number
```

---

### Step 3: Extracting the Encoded Flag Payload
Further deep inspection of the memory strings (`strings mem | grep -i "base64"`) uncovered a specific Base64-encoded string associated with the SMS content and verification steps:

```text
XlR4X0MNTFlWfGdISghNXGdBV21nDEpdZ0tMandWX2dBV01nTwtKfWdZWgldZ0wIZ1xdbF1bTGdMUAkcZ0hQUQ1QUVYBRQ==
```

According to the challenge hint discovered in the memory dump:
> *"by default the sms is base64 encoded, but the flag is (base64 encoded * 2) and xored with number"*

---

### Step 4: Decoding and Decrypting with Python
To decode the payload, we wrote a Python script to perform the Base64 decoding step followed by a byte-level XOR brute-force across standard numeric keys found in the device logs:

```python
import base64

encoded_str = "XlR4X0MNTFlWfGdISghNXGdBV21nDEpdZ0tMandWX2dBV01nTwtKfWdZWgldZ0wIZ1xdbF1bTGdMUAkcZ0hQUQ1QUVYBRQ=="
decoded = base64.b64decode(encoded_str)

# Iterating through possible keys to find the correct XOR offset
for key in range(1, 256):
    xored = bytes([b ^ key for b in decoded])
    if b"5tanD" in xored or b"flag" in xored.lower() or b"{" in xored:
        print(f"Key {key}: {xored}")
```

*Result:* Running the script with **Key 56** successfully decrypted the payload into the plaintext flag:

```text
flag{xxxxxx_xxxxxx_xx_xx_xxxxx_xxxxxx}
```

![Python Script Execution & Flag Discovery](image_9ae19e.png)

---

## Conclusion
By properly extracting the memory dump, tracking the phishing indicators via `strings`, and reversing the custom encoding rule (Base64 + XOR transformation), we successfully uncovered the flag and solved the challenge! 🎯🚀