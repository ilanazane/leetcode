def reverse(input: int) -> int:
    """

    :param input:
    :returns reversed input:

    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21
    """

    string = str(input)
    reverse = ""
    symbol = ""
    for i in string[::-1]:
        if i.isdigit():
            reverse += i
        else:
            symbol += i

    final = symbol + reverse

    return int(final)


input = 120
output = reverse(input)

print(output)
