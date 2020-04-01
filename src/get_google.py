import requests


def get_from_googledrive(url, destination):
    idx = url.find('id=')
    id = url[idx + 3:]

    URL = 'https://docs.google.com/uc?export=download'

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)

    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

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
    url = 'https://drive.google.com/open?id=14cdKEQYaxw8q69-_pbM3F_gsK84eD9N0'
    destination = '../output/google_sample.csv'
    get_from_googledrive(url, destination)
