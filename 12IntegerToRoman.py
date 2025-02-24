"""
Input: num = 3749

Output: "MMMDCCXLIX"
"""


def integerToRoman(input):
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    roman = ""

    for key, value in roman_numerals.items():

        while input >= value:
            roman += key
            input -= value

    return roman


output = integerToRoman(3749)
print(output)
