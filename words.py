def print_upper_words(words):
    """Print each word on seperate line, uppercased.
    
        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())

    
def print_upper_words2(words):
    """Print each word on seperate line, uppercased, if start with E or e.
    
        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on seperate line, upercased, if starts with one of given
    
        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                     must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break