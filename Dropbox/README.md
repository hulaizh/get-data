# Dropbox

1. Register a new Dropbox App api

Create a new app in the [App Console](https://www.dropbox.com/developers/apps), get and save  the access token to `token.txt`.

```txt
dropbox: 54L35GF0...
```

2. Install Dropbox package
   
```txt
pip install dropbox
```

3. Specify the files or folder in the `dropbox.py` to download

```python
# Line 17-21
# download files
dbx_path = '/sharing' # file path on Dropbox
local_path = '/Users/hulai/Desktop' # local path
file_names = ['Bryan  Everett.xlsx', 'Bryan  Everett.dta'] # files to be downloaded
```

```python
# Line 18-19
# download the whole folder
dbx_path = '/sharing' # file path on Dropbox, to be downloaded
local_path = '/Users/hulai/Desktop' # local path
```

After specifying the files or the folder, you can run `dropbox.py` to download.