import string

from nltk import re
import nltk

from nltk.corpus import stopwords

regex_patterns = {
    'url': re.compile(
        r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z'
        r'0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})')
}


def get_emojis_pattern():
    try:
        # UCS-4
        emojis_pattern = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        emojis_pattern = re.compile(
            u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return emojis_pattern


def get_hashtags_pattern():
    return re.compile(r'#\w*')


def get_single_letter_words_pattern():
    return re.compile(r'(?<![\w\-])\w(?![\w\-])')


def get_blank_spaces_pattern():
    return re.compile(r'\s{2,}|\t')


def get_twitter_reserved_words_pattern():
    return re.compile(r'(RT|rt|FAV|fav|VIA|via)')


def get_mentions_pattern():
    return re.compile(r'@\w*')


def get_facebook_reserved_words_pattern():
    return re.compile(r'^(TODO|STH|ELSE)')


class TwitterPreprocessor:

    def __init__(self, text: str):
        self.text = text

    def full_preprocess(self):
        return self.remove_urls() \
            .remove_mentions() \
            .remove_hashtags() \
            .remove_twitter_reserved_words() \
            .remove_punctuation() \
            .remove_single_letter_words() \
            .remove_blank_spaces() \
            .remove_stopwords() \
            .remove_profane_words() \
            .remove_numbers()

    def remove_urls(self):
        self.text = re.sub(pattern=regex_patterns['url'], repl='', string=self.text)
        return self

    def remove_punctuation(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self

    def remove_mentions(self):
        self.text = re.sub(pattern=regex_patterns.get_mentions_pattern(), repl='', string=self.text)
        return self

    def remove_hashtags(self):
        self.text = re.sub(pattern=regex_patterns.get_hashtags_pattern(), repl='', string=self.text)
        return self

    def remove_twitter_reserved_words(self):
        self.text = re.sub(pattern=re.compile(r'(RT|rt|FAV|fav|VIA|via|AMP|amp)'), repl='', string=self.text)
        return self

    def remove_single_letter_words(self):
        self.text = re.sub(pattern=regex_patterns.get_single_letter_words_pattern(), repl='', string=self.text)
        return self

    def remove_blank_spaces(self):
        self.text = re.sub(pattern=regex_patterns.get_blank_spaces_pattern(), repl=' ', string=self.text)
        return self

    def remove_stopwords(self, extra_stopwords):
        text_list = list(self.text)
        self.text = set(text_list) - set(stopwords.words(self.language)) - set(extra_stopwords)
        return self

    def remove_profane_words(self):
        text_list = list(self.text)
        self.text = set(text_list) - set(self._get_profane_words())
        return self

    # def __tokenize_to_list__(self, text):
    #     tokens = nltk.wordpunct_tokenize(text)
    #     text = nltk.Text(tokens)
    #     return [w.lower() for w in text if w.isalpha() or w.isalnum()]

    def remove_numbers(self):
        text_list = list(self.text)
        for text in text_list:
            if text.isnumeric():
                # if the number is not a year, remove it
                if int(text) < 1900 or int(text) > 2100:
                    text_list.remove(text)

        self.text = ''.join(text_list)
        return self

    def _get_profane_words(self):
        if self.language == 'en':
            return vars.en_profane_words
        elif self.language == 'nl':
            return vars.nl_profane_words
        elif self.language == 'de':
            return vars.de_profane_words
        else:
            return vars.el_profane_words
