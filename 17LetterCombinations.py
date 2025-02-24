"""
letter combinations of a phone number 


"""


def letterCombinations(digits: str) -> str:
    """
    Description:
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.
    Return the answer in any order.

    :param digits:
    :returns array of letter combinations:

    Example 1:

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    """
    import itertools

    phone_letters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    letters_array = []

    for i in digits:
        digit = int(i)
        letters_array.append(list(phone_letters[digit]))

    out = []
    # find the cartesian product
    for i in list(itertools.product(*letters_array)):
        # combine letters from each number into a str
        x = "".join(i)

        out.append(x)

    return out


digits = "23"
output = letterCombinations(digits)
print(output)
