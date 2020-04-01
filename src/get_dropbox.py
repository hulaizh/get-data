import urllib.request


def get_from_dropbox(url, destination):

    if url.endswith('dl=1'):
        URL = url
    elif url.endswith('dl=0'):
        URL = url.replace('dl=0', 'dl=1')
    else:
        print('False link! Please copy the right link.')
        raise Exception

    if URL:
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

        with open(destination, 'wb') as f:
            f.write(data)


if __name__ == "__main__":
    url = "https://www.dropbox.com/s/221s9p8p8fap61x/Bryan%20%20Everett.xlsx?dl=0"
    destination = '../output/dropbox_sample.csv'
    get_from_dropbox(url, destination)
