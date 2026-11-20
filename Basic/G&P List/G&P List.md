# G&P+lists - Digital Forensics Writeup

## Challenge Description
Just Open the File and Capture the flag. Submission in MD5.

File:
`G&P+lists.docx`

![Challenge Description](../../images/G%26P%20List/1.png)

---

## Opening the File
The file was opened using LibreOffice Writer and appeared normal with no visible suspicious content.

![Opening Document](../../images/G%26P%20List/2.png)

---

## Analysis with Binwalk
Since `.docx` files are ZIP archives, I used:

```bash
binwalk G&P+lists.docx

```
![3](../../images/G%26P%20List/3.png)

## Extracting Files

To extract embedded data:

```bash
binwalk -e G&P+lists.docx

```


## Reading the Flag

```bash
cat Flag.txt

```

![3](../../images/G%26P%20List/4.png)

Output:

```
877c1fa0445adaedc5365d9c139c5219

```

