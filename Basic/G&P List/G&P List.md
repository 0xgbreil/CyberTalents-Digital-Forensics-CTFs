# G&P+lists - Digital Forensics Writeup

## Challenge Description
Just Open the File and Capture the flag. Submission in MD5.

File:
`G&P+lists.docx`

![Challenge Description](1.png)

---

## Opening the File
The file was opened using LibreOffice Writer and appeared normal with no visible suspicious content.

![Opening Document](2.png)

---

## Analysis with Binwalk
Since `.docx` files are ZIP archives, I used:

```bash
binwalk G&P+lists.docx

```
![3](3.png)

## Extracting Files

To extract embedded data:

```bash
binwalk -e G&P+lists.docx

```


## Reading the Flag

```bash
cat Flag.txt

```

![3](4.png)

Output:

```
877c1fa0445adaedc5365d9c139c5219

```

