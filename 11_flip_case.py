def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flip = ''

    for letter in range(len(phrase)):
        up_ltr = phrase[letter].upper()
        
        if to_swap.upper() == up_ltr:
            if up_ltr == phrase[letter]:
                flip += to_swap.lower()
            else:
                flip += to_swap.upper()
        else:
            flip += phrase[letter]
    
    return flip
