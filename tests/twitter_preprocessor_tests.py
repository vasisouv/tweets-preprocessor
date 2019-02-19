import unittest
from twitter_preprocessor import TwitterPreprocessor
from tests.test_cases_generator import TestCasesGenerator


class Tests(unittest.TestCase):
    def test_remove_urls(self):
        for test_case in TestCasesGenerator.urls:
            preprocessor = TwitterPreprocessor(text=test_case['init'])
            self.assertEqual(test_case['expected'], preprocessor.remove_urls().text)

    def test_remove_punctuation(self):
        for test_case in TestCasesGenerator.punctuation:
            preprocessor = TwitterPreprocessor(text=test_case['init'])
            self.assertEqual(test_case['expected'], preprocessor.remove_punctuation().text)

    # def test_remove_urls_one_at_the_end(self):
    #     self.assertEqual('Delighted to have been awarded the first ever TerraPMC Fellowship '
    #                      'offered by @TerraAmArt and @PaulMellonCentr! Wil… ',
    #                      self.preprocessor.remove_urls__(self.url_tweets[1]))
    #
    # def test_remove_urls_buggy_url(self):
    #     self.assertEqual('canbe foundat',
    #                      self.preprocessor.__remove_urls__(self.url_tweets[7]))
    #
    # def test_remove_urls_multiple_urls(self):
    #     self.assertEqual('RT @JHSMlCDROP:  '
    #                      'Friendly reminder this art exist.  ',
    #                      self.preprocessor.__remove_urls__(self.url_tweets[6]))
    #
    # # tweet texts should stay the same - multiple spaces/tab test
    # def test_remove_misc_no_matches(self):
    #     self.assertEqual(self.misc_tweets[0],
    #                      self.preprocessor.__remove_misc__(self.misc_tweets[0]))
    #
    # def test_remove_misc_spaces(self):
    #     self.assertEqual(' push it to the limit and to the lim it',
    #                      self.preprocessor.__remove_misc__(self.misc_tweets[1]))
    #
    # # tweet texts should stay the same - singe letter tests
    # def test_remove_misc_no_matches2(self):
    #     self.assertEqual('sap not sap test0 te st as cc',
    #                      self.preprocessor.__remove_misc__(self.misc_tweets[2]))
    #
    # # Years (range [1900 -> 2100]) should remain while other numbers should vanish from the list
    # def test_remove_numbers_but_not_years(self):
    #     text = "Should remove number 123, not 2020, yes 2500"
    #     self.assertEqual(['should', 'remove', 'number', 'not', '2020', 'yes'],
    #                      self.preprocessor.__remove_numbers__(self.preprocessor.__tokenize_to_list__(text)))


if __name__ == '__main__':
    unittest.main()
