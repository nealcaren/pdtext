from time import sleep
from .slugify import slugify
import requests


def locate(url, directory = 'html'):
    '''Create file name and place in directory'''
    file_name = slugify(url)
    location = os.path.join(directory, file_name)
    return location

def open_html(url, directory = 'html'):
    """Attempt to open a file based on the url."""
    location = locate(url)

    with open(location, "r") as infile:
        html = infile.read()

    return html

def get_html(url, directory = 'html', pause = 1):
    """Download & save html text using the url to create the filename."""
    pause(3)
    r = requests.get(url)
    html = r.text

    location = ocate(url, directory = directory)

    with open(location, "w") as outfile:
        outfile.write(html)

    return html


def retrieve_html(url, directory, pause):
    
    try:
        return open_html(url, directory)
    except:
        return get_html(url, directory, pause)
