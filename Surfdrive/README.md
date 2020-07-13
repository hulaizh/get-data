# Surfdrive


1. Get shareable link

Choose the file, share it and get the shareable link.

2. Paste the link to surfdrive.py, change the local name and local path to save the file

```python
# Line 20-23
if __name__ == "__main__":
    url = "https://surfdrive.surf.nl/files/index.php/s/lvcZ8Ob7nDWwXbX"
    destination = '../output/surfdrive_sample.csv'
    get_from_surfdrive(url, destination)
```

After specifying the file, you can run surfdrive.py to download.