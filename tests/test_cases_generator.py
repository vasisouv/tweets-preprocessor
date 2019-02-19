class TestCasesGenerator:
    urls = [
        {
            'init': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. https://example.com',
            'expected': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. ',
        },
        {
            'init': 'Test text.https://t.co/asdas123123 https://t.co/123123asdasddsa. Test123',
            'expected': 'Test text.  Test123'
        }
    ]

    punctuation = [
        {
            'init': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. https://example.com',
            'expected': 'Lorem ipsum dolor sit amet consectetur adipiscing elit Phasellus rhoncus httpsexamplecom'
        }
    ]
