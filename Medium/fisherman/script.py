import base64

encoded_str = "XlR4X0MNTFlWfGdISghNXGdBV21nDEpdZ0tMandWX2dBV01nTwtKfWdZWgldZ0wIZ1xdbF1bTGdMUAkcZ0hQUQ1QUVYBRQ=="
decoded = base64.b64decode(encoded_str)

# تجربة مفاتيح الـ XOR المحتملة من محتوى الـ SMS (مثل أرقام متكررة أو مفتاح بسيط)
for key in range(1, 256):
    xored = bytes([b ^ key for b in decoded])
    if b"cyber" in xored.lower() or b"flag" in xored.lower() or b"{" in xored:
        print(f"Key {key}: {xored}")
