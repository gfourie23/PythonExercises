def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = []
    for char in phrase:
        if char.lower() in to_swap:
            swapped_char = char.upper() if char.islower() else char is char.lower()
            swapped.append(swapped_char)
        else:
            swapped.append(char)
    return swapped
    
   
