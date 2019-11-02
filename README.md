## Tweets Preprocessor

<p align="center">
  <br>
    <img width="100" src="./ptwist_logo.png">
    <img width="100" src="./twitter_logo.png">
  <br>
  <br>
</p>

The tweets preprocessor module, developed by the AUTH team 
as part of the [PlasticTwist Crowdsourcing module](https://crowdsourcing.plastictwist.com)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

## Installation
The `tweets-preprocessor` module is not yet available trough PyPI, thus requiring manual import.

```
$ pip install -r requirements.txt
```
then execute `utils/requirements_installer.py` to install additional dependencies automatically.


## Usage

The module was developed in a functional way and features a Fluent API. This allows the user
to either call individual pre-processing methods or use the `full_preprocess` method to
apply all of the pre-processing methods to his text.

The list of methods that can currently be used are:

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
    * has an `preserve_years` parameter (boolean) that allows users to choose whether or not
    years should be removed.
    
### Examples

#### Using specific methods

```python
from twitter_preprocessor import TwitterPreprocessor

p = TwitterPreprocessor('Some @ptwist text to be preprocessed. It contains 2 sentences. Best text 2019!')

p.remove_mentions().remove_punctuation().remove_numbers(preserve_years=True).remove_blank_spaces()
print(p.text)
# 'Some text to be preprocessed It contains sentences Best text 2019'
```

#### Full pre-processing

```python
from twitter_preprocessor import TwitterPreprocessor

p = TwitterPreprocessor('RT @ptwist This text contains mentions, urls, some Twitter words and some stopwords to be preprocessed via https://example.com.')

p.fully_preprocess()
print(p.text)
# 'This text contains mentions urls Twitter words stopwords preprocessed'
```


## License

This project is licensed under the [MIT license](http://opensource.org/licenses/MIT).

## Credits
Developed and maintained by: [vasisouv](https://github.com/vasisouv), [alextsil](https://github.com/alextsil), [idimitriadis](https://github.com/idimitriadis)
