# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

import re

def getListOfWordsFromListOfSentences(sentences):
    words = [re.sub(r'[.,!?:-]', '', sentence.lower()).split() for sentence in sentences]
    words = [word for nestedList in words for word in nestedList]

    return words

def getHistogramOfWords(words):
    histogram = {}
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def sortHistogramByOccurrences(histogram):
    items = histogram.items()
    sortedData = sorted(items, key=lambda el: el[1], reverse=True)
    sortedHistogram = [{'word': el[0], 'count': el[1]} for el in sortedData]

    return sortedHistogram

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

words = getListOfWordsFromListOfSentences(sentences)
histogram = getHistogramOfWords(words)
sortedHistogram = sortHistogramByOccurrences(histogram)

for index in range(3):
    listCounter = str(index + 1) + "."
    word = sortedHistogram[index]
    print(listCounter, '"' + word['word'] + '"', '-', word['count'])

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
