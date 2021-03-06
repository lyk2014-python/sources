def sorted_words(result):
    return sorted(result.items(),
                  key=lambda x: x[1],
                  reverse=True)

def count_words(text):
    words = [word for word in text.split()
             if len(word) > 4]
    result = {}

    for word in words:
        if not word in result:
            result[word] = words.count(word)

    return sorted_words(result)
