import unittest

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


class TestSuite(unittest.TestCase):
    def test_all_unique(self):
        self.assertEqual(has_unique_chars("asdfghjkl"), True)

    def test_all_unique_2(self):
        self.assertEqual(has_unique_chars("wepto"), True)

    def test_all_unique_3(self):
        self.assertEqual(has_unique_chars("qwertyuiopasdfghjklzxcvbnm"), True)

    def test_non_unique(self):
        self.assertEqual(has_unique_chars("asdhjkla"), False)

    def test_multi_non_unique(self):
        self.assertEqual(has_unique_chars("qwertyuioqwertyu"), False)

    def test_multi_non_unique_2(self):
        self.assertEqual(has_unique_chars("thisisproblematic"), False)


if __name__ == "__main__":
    unittest.main()
