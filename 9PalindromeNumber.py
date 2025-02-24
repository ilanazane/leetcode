# x = 121
# x = -121
# x = 10


def isPalindrome(x: int) -> bool:

    new_x = str(x)

    reversed = ""

    for j in range(len(new_x))[::-1]:
        reversed += new_x[j]

    if new_x == reversed:
        return True
    else:
        return False


import unittest


class Testing(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(isPalindrome(10), False)
        self.assertEqual(isPalindrome(-121), False)
        self.assertEqual(isPalindrome(121), True)


if __name__ == "__main__":
    unittest.main()
