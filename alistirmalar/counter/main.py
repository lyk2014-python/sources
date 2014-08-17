import sys

from readers import read_from_url
from counter import count_words
from printer import print_histogram

if len(sys.argv) > 1:
    text = read_from_url(sys.argv[1])
    words = count_words(text)

    print_histogram(words)
else:
    print "Kullanim: python main.py <url>"