class TestCasesGenerator:
    urls = [
        {
            'case': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. https://example.com',
            'expected': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. ',
        },
        {
            'case': 'Test text.https://t.co/asdas123123 https://t.co/123123asdasddsa. Test123',
            'expected': 'Test text.  Test123'
        }
    ]

    punctuation = [
        {
            'case': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus rhoncus. https://example.com',
            'expected': 'Lorem ipsum dolor sit amet consectetur adipiscing elit Phasellus rhoncus httpsexamplecom'
        }
    ]

    mentions = [
        {
            'case': 'Lorem ipsum @dolor sit amet, @consectetur adipiscing elit.',
            'expected': 'Lorem ipsum  sit amet,  adipiscing elit.'
        }
    ]

    hashtags = [
        {
            'case': 'Lorem 123 #test ipsum #sit #amet #test',
            'expected': 'Lorem 123  ipsum   '
        }
    ]

    twitter_reserved_words = [
        {
            'case': 'RT Lorem ipsum dolor sit via @test. rt please.',
            'expected': ' Lorem ipsum dolor sit  @test.  please.'
        }
    ]

    single_letter_words = [
        {
            'case': 'RT Lorem ipsum a good dog has no g  dolor sit v @test.',
            'expected': 'RT Lorem ipsum  good dog has no   dolor sit  @test.'
        }
    ]

    blank_spaces = [
        {
            'case': 'RT Lorem ipsum  good dog has no   dolor sit  @test.',
            'expected': 'RT Lorem ipsum good dog has no dolor sit @test.'
        }
    ]

    stopwords = [
        {
            'case': 'This is a nice evening here at the bar.',
            'expected': 'This nice evening bar .'
        }
    ]

    profane_words = [
        {
            'case': 'This fucking evening at this shit bar is the worst.',
            'expected': 'This evening at this bar is the worst.'
        }
    ]
