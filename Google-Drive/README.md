# Google Drive

>TODO: 
>Use PyDrive2 to download files and folders in Google Drive.
>
>Requirement: self-owned domain (excluding Github pages a like) due to Google's new restrictions.

1. Get shareable link

Choose the file and click the `Get shareable link`, then choose `Anyone on the internet with this linkcan view `, and copy the link.

2. Paste the link to googledrive.py, change the local name and local path to save the file

```python
# Line 50-54
if __name__ == "__main__":
    url = 'https://drive.google.com/file/d/1oU6kHooFJVklVsM0EMvMzv1FBpb856qw/view?usp=sharing'
    lpath = 'Google-Drive/'
    lname = 'Bryan Evertt.xlsx'
    get_from_googledrive(url, lpath, lname)
```

After specifying the file, you can run googledrive.py to download.