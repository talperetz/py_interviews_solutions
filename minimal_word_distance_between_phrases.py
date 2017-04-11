#!/usr/bin/env python

"""
:Date: 4/8/2017

:TL;DR: find sentence with minimal word-distance between two phrases in a given text

:Abstract: home assignment from Gartner

:Problem: You get Text, 2 phrases and negation word.
You have to find where is the place in the text where there is a minimal word-distance between the two phrases
within the same sentence and where the negation word do not appear in the middle.
* Sentence is ended by those 2 options only: period (.) or 3 exclamation marks (!!!)
* Words are divided by those 2 options only: space or comma
* You can ignore the other signs, you can assume no initials or acronyms so make it simple.
* Phrase can consist of more than one word.

:Proposed Solution:
parse text into sentences with words
filter all sentences without both phrases or containing negation word in between phrases
find sentence* with minimal word-distance between two phrases
return sentence* and minimal word-distance
"""

import re
import sys

__author__ = "Tal Peretz"
__copyright__ = "Copyright 2017"
__credits__ = ["Tal Peretz"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Tal Peretz"
__email__ = "talperetz24@gmail.com"
__status__ = "Development"


class PhrasesSentence:
    """representation of sentence with two phrases in it"""

    def __init__(self, whole, phrase1, phrase2):
        self.whole_sentence = whole
        self.first_phrase = min(phrase1, phrase2, key=lambda phrase: whole.find(phrase))
        self.last_phrase = max(phrase1, phrase2, key=lambda phrase: whole.find(phrase))
        self.first_phrase_index = whole.find(self.first_phrase)
        self.last_phrase_index = whole.find(self.last_phrase)
        self.between_phrases = whole[self.first_phrase_index + len(self.first_phrase):self.last_phrase_index]

    def is_both_phrases_in_sentence(self):
        """return True if both phrases in sentence"""
        return self.first_phrase_index != -1 and self.last_phrase_index != -1

    def is_word_between_phrases(self, word):
        """return True if word is between the two phrases in the sentence"""
        return word in self.between_phrases if self.is_both_phrases_in_sentence() else False

    def get_word_distance_between_phrases(self):
        """return num of words between two phrases in the sentence"""
        assert self.is_both_phrases_in_sentence(), "both phrases must be in sentence"
        words_list = parse_sentence_to_words(self.between_phrases)
        return len(words_list)


def parse_text_to_sentences(text):
    """
    given :param text: string :return: list of sentences split according to '.' or '!!!'
    """
    assert isinstance(text, str), "text must be string"
    return re.split(r'\.|!!!', text)


def parse_sentence_to_words(sentence):
    """
    given :param sentence: string :return: list of words split according to space or comma
    """
    assert isinstance(sentence, str), "sentence must be string"
    return re.split(r'\s|,', sentence)[1:-1]  # split returns two empty strings at the end and start


def get_min_word_distance_sentence(text, phrase1, phrase2, negation_word):
    """
    :param text: string
    :param phrase1: string
    :param phrase2: string
    :param negation_word: string
    :return: sentence with minimal word-distance between phrase1 and phrase2
    """
    # text to list of sentences
    sentences = parse_text_to_sentences(text)
    phrased_sentences = [PhrasesSentence(sentence, phrase1, phrase2) for sentence in sentences]

    # filtering irrelevant sentences
    relevant_sentences = [sentence for sentence in phrased_sentences if
                          sentence.is_both_phrases_in_sentence() and not sentence.is_word_between_phrases(
                              negation_word)]

    # find min word-distance between phrases in relevant sentences
    min_word_distance_sentence = min(relevant_sentences,
                                     key=lambda sentence: sentence.get_word_distance_between_phrases())
    return min_word_distance_sentence


if __name__ == '__main__':
    min_word_distance_sentence = get_min_word_distance_sentence(*sys.argv[1:])

    print(min_word_distance_sentence.whole_sentence, min_word_distance_sentence.between_phrases,
          min_word_distance_sentence.get_word_distance_between_phrases())
