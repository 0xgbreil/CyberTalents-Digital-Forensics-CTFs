# Message in a Bottle     Challenge Description
That's so easy. Just Capture the Flag

![Challenge Description](../../images/Message%20in%20a%20Bottle/1.png)

---

## File Identification
To determine the file type, the following command was used:

```bash
file message-in-bottle.png
```

![2](../../images/Message%20in%20a%20Bottle/2.png)

## Steganography Analysis

After multiple attempts to analyze the image, a suitable tool was identified: **OpenStego** (version 0.6.1).

Download link:  
https://github.com/syvaidya/openstego/releases/tag/openstego-0.6.1

This tool was used to extract hidden data from the image.

![3](../../images/Message%20in%20a%20Bottle/3.png)

## Extracting Hidden Data

Load the image into OpenStego, specify the output location, then choose the "Extract Data" option to retrieve the hidden content.

![4](../../images/Message%20in%20a%20Bottle/4.png)

## Final Flag

The Flag is :

```bash
Flag{701_L@b$_CTF0}
```