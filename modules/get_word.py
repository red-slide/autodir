async def get_word(charset, length_range, last_word=None):
    # Converts the charset to a list and creates a dictionary for quick access
    charset = sorted(set(charset))  # Ensures charset is sorted and unique
    charset_dict = {char: index for index, char in enumerate(charset)}
    
    min_len, max_len = length_range

    if last_word is None:
        # Generates the first word for the minimum length
        return charset[0] * min_len
    
    # Converts the last word into a list of indices
    indices = [charset_dict[char] for char in last_word]
    
    # Increments the last word
    for i in reversed(range(len(indices))):
        if indices[i] < len(charset) - 1:
            indices[i] += 1
            break
        indices[i] = 0
    else:
        # If we are here, we need to add a new character at the beginning
        indices = [0] * (len(indices) + 1)
    
    # Converts indices back to characters
    next_word = ''.join(charset[i] for i in indices)
    
    # If the generated word is longer than the maximum length, returns None
    if len(next_word) > max_len:
        return None
    
    return next_word
