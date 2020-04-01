import ftplib
# import os


def get_from_ftp(agent, path, filename=None, destination=''):

    host = agent['host']
    user = agent['user']
    passwd = agent['passwd']

    ftp = ftplib.FTP(host, user, passwd)
    ftp.cwd('path')

    if filename:
        with open(destination, 'wb') as f:
            ftp.retrbinary(filename, f.write)
    else:
        raise Exception

    ftp.quit()


if __name__ == "__main__":
    agent = {'host': 'ftp.ncbi.nih.gov', 'user': 'anonymous', 'passwd': ''}
    path = '/pub/GeneTests'
    filename = 'disease_OMIM_Gene_US.txt'  # Permission Denied
    destination = '../output/ftp_sample.txt'
    get_from_ftp(agent, path, filename, destination)
