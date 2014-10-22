from urllib.parse import urlparse
from urllib.request import urlopen

__author__ = 'David Moreno García'


def read(url):
    if urlparse(url).scheme == '':
        # Assume that this is a file and use 'file:' scheme
        schemed_url = 'file:{}'.format(url)
    try:
        content = urlopen(schemed_url).read().decode('utf-8')
    except:
        # try with 'http://'
        schemed_url = 'http://{}'.format(url)
        try:
            content = urlopen(schemed_url).read().decode('utf-8')
        except:
            content = ""

    return content