import urllib.request


def get_from_surfdrive(url, destination):

    if url.endswith('download'):
        URL = url
    else:
        URL = '/'.join((url, 'download'))

    if URL:
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

        with open(destination, 'wb') as f:
            f.write(data)


if __name__ == "__main__":
    url = "https://surfdrive.surf.nl/files/index.php/s/lvcZ8Ob7nDWwXbX"
    destination = '../output/surfdrive_sample.csv'
    get_from_surfdrive(url, destination)
