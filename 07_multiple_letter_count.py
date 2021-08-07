def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequencycounter = {}
    for letter in phrase:
        if letter not in frequencycounter:
            frequencycounter[letter] = 1
        else:
            frequencycounter[letter] = frequencycounter[letter] + 1

    return frequencycounter
