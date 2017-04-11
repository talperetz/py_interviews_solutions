#!/usr/bin/env python

"""
:Date: 4/9/2017
"""

import unittest
import minimal_word_distance_between_phrases

__author__ = "Tal Peretz"
__copyright__ = "Copyright 2017"
__credits__ = ["Tal Peretz"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Tal Peretz"
__email__ = "talperetz24@gmail.com"
__status__ = "Development"


class SimpleTestCase(unittest.TestCase):
    def test_given_text(self):
        text = "John Doe aaa bbb ccc ddd love music. John Doe aaa not love music."
        phrase1 = "John Doe"
        phrase2 = "love music"
        negation_word = "not"
        min_word_distance_sentence = minimal_word_distance_between_phrases.get_min_word_distance_sentence(text, phrase1,
                                                                                                          phrase2,
                                                                                                          negation_word)
        self.assertEqual(min_word_distance_sentence.whole_sentence, "John Doe aaa bbb ccc ddd love music")
        self.assertEqual(min_word_distance_sentence.get_word_distance_between_phrases(), 4)

    def replace_phrases_position(self):
        text = "John Doe aaa bbb ccc ddd love music. John Doe aaa not love music."
        phrase1 = "love music"
        phrase2 = "John Doe"
        negation_word = "not"
        min_word_distance_sentence = minimal_word_distance_between_phrases.get_min_word_distance_sentence(text, phrase1,
                                                                                                          phrase2,
                                                                                                          negation_word)
        self.assertEqual(min_word_distance_sentence.whole_sentence, "John Doe aaa bbb ccc ddd love music")
        self.assertEqual(min_word_distance_sentence.get_word_distance_between_phrases(), 4)

    def test_more_than_two_sentences(self):
        text = "John Doe winner love music. John Doe aaa not love music. John Doe aa bbb ccc ddd love " \
               "music. John Doe aaa ddd love music. John Doe aaa bbb ccc ddd a love music."
        phrase1 = "John Doe"
        phrase2 = "love music"
        negation_word = "not"
        min_word_distance_sentence = minimal_word_distance_between_phrases.get_min_word_distance_sentence(text, phrase1,
                                                                                                          phrase2,
                                                                                                          negation_word)
        self.assertEqual(min_word_distance_sentence.whole_sentence, "John Doe winner love music")
        self.assertEqual(min_word_distance_sentence.get_word_distance_between_phrases(), 1)


if __name__ == '__main__':
    unittest.main()
