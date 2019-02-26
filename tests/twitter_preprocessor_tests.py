import unittest
from twitter_preprocessor import TwitterPreprocessor
from tests.test_cases_generator import TestCasesGenerator


class Tests(unittest.TestCase):
    def _generate_tests(self, module: str, method: str):
        for test_case in getattr(TestCasesGenerator, module):
            text = getattr(TwitterPreprocessor(text=test_case['case']), method)().text
            self.assertEqual(test_case['expected'], text)

    def test_remove_urls(self):
        self._generate_tests('urls', 'remove_urls')

    def test_remove_punctuation(self):
        self._generate_tests(module='punctuation', method='remove_punctuation')

    def test_remove_mentions(self):
        self._generate_tests(module='mentions', method='remove_mentions')

    def test_remove_hashtags(self):
        self._generate_tests(module='hashtags', method='remove_hashtags')

    def test_remove_twitter_reserved_words(self):
        self._generate_tests(module='twitter_reserved_words', method='remove_twitter_reserved_words')

    def test_remove_single_letter_words(self):
        self._generate_tests(module='single_letter_words', method='remove_single_letter_words')

    def test_remove_blank_spaces(self):
        self._generate_tests(module='blank_spaces', method='remove_blank_spaces')

    def test_remove_stopwords(self):
        self._generate_tests(module='stopwords', method='remove_stopwords')

    def test_remove_profane_words(self):
        self._generate_tests(module='profane_words', method='remove_profane_words')


if __name__ == '__main__':
    unittest.main()
