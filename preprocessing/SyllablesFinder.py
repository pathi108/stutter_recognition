from nltk.corpus import cmudict
import string
d = cmudict.dict()
def nsyl(word):
  return [list(y for y in x if y[-1].isdigit()) for x in d[word.lower()]]


def syllablesForSentence(text):
    for word in text.split():
        print(nsyl(word.strip(string.punctuation)))