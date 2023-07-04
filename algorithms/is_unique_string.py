LC_LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def has_unique_chars(input: str):
    # Uses a byte array to keep track of characters in string
    char_bool_array = 0
    for char in input:
        offset = LC_LETTERS.find(char)
        if char_bool_array & (1 << offset) > 0:
            return False
        char_bool_array |= 1 << offset
    return True
