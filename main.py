from twitter_preprocessor import TwitterPreprocessor

if __name__ == '__main__':
    p = TwitterPreprocessor(text='Test123 https://www.tsikos.gr !! .. , ')

    p.remove_urls().remove_punctuation()
    print(p.text)
    print(type(p.text))
