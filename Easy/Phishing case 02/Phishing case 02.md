# Phishing Case 02 - Digital Forensics Writeup

## Challenge Description
We have received a phishing email, analyze it and answer:

- **X:** IP address of the sender?
- **Y:** What is the phishing URL? (sub.domain.tld)

Flag format: `flag{X:Y}`

![Challenge Description](../../images/Phishing%20case%2002/1.png)

---

## Email Analysis

After downloading the provided `.eml` file, I opened it using a text editor to inspect the email headers and content.

By examining the `Received` header, I identified the sender's IP address:

```text
209.58.149.98
````
![Image](../../images/Phishing%20case%2002/2.png)

## **Extracting the Phishing URL**

While reviewing the email, I found a Base64-encoded section containing additional information.

![Image](../../images/Phishing%20case%2002/3.png)

I copied the encoded content and decoded it using [CyberChef](https://gchq.github.io/CyberChef/?utm_source=chatgpt.com), applying the **From Base64** operation.

The decoded content revealed the phishing URL:

```
ohmyomy1.000webhostapp.com
```
![Image](../../images/Phishing%20case%2002/4.png)

![Image](../../images/Phishing%20case%2002/5.png)

## **Final Flag**

```
flag{209.58.149.98:ohmyomy1.000webhostapp.com}
```
