# TODO
# allow several days for Google to verify the OAuth
# need a self-owned domain
# PyDrive2 to manage drive files

# from pydrive2.auth import GoogleAuth

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()

import requests
import os


def get_from_googledrive(url, lpath, lname):
    id0 = url.find('/d/')
    id1 = url.find('/view')

    id = url[id0 + 3: id1]

    URL = 'https://docs.google.com/uc?export=download'

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)

    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    destination = os.path.join(lpath, lname)
    CHUNK_SIZE = 32768
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
        else:
            print('False link! Please copy the right link.')
            raise Exception


if __name__ == "__main__":
    url = 'https://drive.google.com/file/d/1oU6kHooFJVklVsM0EMvMzv1FBpb856qw/view?usp=sharing'
    lpath = 'Google-Drive/'
    lname = 'Bryan Evertt.xlsx'
    get_from_googledrive(url, lpath, lname)
