from readers import read_from_file
from counter import count_words
from printer import print_histogram

FILE_PATH = "data.txt"

text = read_from_file(FILE_PATH)
words = count_words(text)

print_histogram(words)