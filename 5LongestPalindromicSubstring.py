def invert(a_string: str) -> str:
    """
    return a reversed string

    :param str: a string of characters
    :returns str: reversed string of characters
    """

    inverted = ""
    for i in a_string[::-1]:
        inverted += i
    return inverted


def longestPalindrome(s: str) -> str:
    """
    :param str: strings of characters
    :returns str: longest palindrome string
    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    Example 2:

    Input: s = "cbbd"
    Output: "bb"
    """
    palindrome_strings = []

    for i in range(len(s)):
        # left pointer
        start = i
        # right pointer
        end = len(s)

        while start != end:
            # get substring
            substring = s[start:end]
            # reverse substring
            inverse_substring = invert(substring)
            # check if palindrome and length is greater than 1
            if substring == inverse_substring:
                palindrome_strings.append(substring)
            # decrease pointer
            end -= 1

    return max(palindrome_strings, key=len)


input = "babad"
print("output: ", longestPalindrome(input))
