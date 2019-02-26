## PlasticTwist Crowdsourcing Twitter Preprocessor

<p align="center">
  <br>
    <img width="200" src="./ptwist_logo.png">
    <img width="200" src="./twitter_logo.png">
  <br>
  <br>
</p>

> Repo containing the Twitter preprocessor module, developed by the AUTH OSWinds team

## Installation
The `tweets-preprocessor` module is not yet up in PyPI, thus requiring manual import.

For minimal setup for English you need to install `profanity-filter` with is bundled with `spacy` and download `spacy`
model for tokenization and lemmatization as well as nltk:
```
$ pip install -r requirements.txt
$ > run utils/requirements_installer.py
```

## Usage

The module is created in a functional way with a Fluent API. Thus, the user
can either call individual methods or use the `full_preprocess` method to
apply all of our preprocessing methods to his text.

The list of methods that can be used are:

* `remove_urls` - Removes all urls (e.g. 'https://ptwist.eu')
* `remove_mentions` - Removes all mentions (e.g. '@PlasticTwistBot')
* `remove_hashtags` - Removes all hashtags (e.g. '#plastictwist')
* `remove_twitter_reserved_words` - Removes Twitter reserved words (e.g. 'RT', 'via')
* `remove_punctuation` - Removes punctuation (e.g. '.', '!')
* `remove_single_letter_words` - Removes single-letter words (e.g. 'b', 'f')
* `remove_blank_spaces` - Removes blank spaces
* `remove_stopwords` - Removes stopwords (e.g. 'a', 'at', 'here')
    * has an `extra_stopwords` parameter (list) that allows users to add extra stopwords
* `remove_profane_words` - Removes profane words
* `remove_numbers` - Removes numbers (e.g. '2', '999')
    * has an `remove_years` parameter (boolean) that allows users to choose whether or not
    years should be deleted.
    
### Examples

```python
from twitter_preprocessor import TwitterPreprocessor

p = TwitterPreprocessor('Some text to be preprocessed')
```

## Credits
English profane word dictionary: https://github.com/areebbeigh/profanityfilter/ (author Areeb Beigh).

Russian profane word dictionary: https://github.com/PixxxeL/djantimat (author Ivan Sergeev).