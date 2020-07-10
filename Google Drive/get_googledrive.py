from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# import os

# Authenticate and create the PyDrive client.
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

local_path = '/Users/hulai/Desktop'


file_list = drive.ListFile(
    {'q': "'sharing' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))


# # 2. Auto-iterate using the query syntax


# #    https://developers.google.com/drive/v2/web/search-parameters
# file_list = drive.ListFile(
#     {'q': "'15m9KTGiLT0kfN7mFBhtuxCtdSCDZz3qq' in parents"}).GetList()  # use your own folder ID here

# for f in file_list:
#     # 3. Create & download by id.
#     print('title: %s, id: %s' % (f['title'], f['id']))
#     fname = f['title']
#     print('Downloading to {}'.format(local_path))
#     f_ = drive.CreateFile({'id': f['id']})
#     f_.GetContentFile(fname)
