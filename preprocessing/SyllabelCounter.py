from nltk.corpus import cmudict
import string

phoneme_dict = dict(cmudict.entries())
def syllables_in_text(text):
    return [syllables_in_word(word.strip(string.punctuation)) for word in text.split()]


def syllables_in_word(word):
    if phoneme_dict.has_key(word):
        return [ph for ph in phoneme_dict[word] if ph.strip(
            string.letters)]
    else:
        return []