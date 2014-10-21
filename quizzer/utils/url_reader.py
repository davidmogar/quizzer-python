from urllib.parse import urlparse
from urllib.request import urlopen

__author__ = 'David Moreno García'


def read(url):
    if urlparse(url).scheme == '':
        # Assume that this is a file and use 'file:' scheme
        url = 'file:{}'.format(url)
    try:
        content = urlopen(url).read().decode('utf-8')
    except:
        content = ""

    return content