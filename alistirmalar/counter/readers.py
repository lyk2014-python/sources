import requests
import re

def strip_tags(data):
    return re.sub(r'<[^>]*?>', '', data)

def read_from_file(path):
    return open(path).read()

def read_from_url(url):
    data = requests.get(url).content
    return strip_tags(data)
