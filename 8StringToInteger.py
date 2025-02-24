# s = "42"
# s = " -042"
# s = "1337c0d3"
# s = "0-1"
# s = "words and 987"


def myAtoi(input: str) -> int:

    integers = ""
    symbol = ""

    # remove white spaces before doing anything
    removed_spaces = " ".join(input.split())

    for i in range(len(removed_spaces)):
        # check if a digit
        if removed_spaces[i].isdigit():
            integers += removed_spaces[i]
        # check if a leading negative sign
        elif removed_spaces[i] == "-" and i == 0:
            symbol += removed_spaces[i]
        # if neither, then break
        else:
            break

    # concat symbol and integers
    final = symbol + integers
    try:
        return int(final)
    except:
        return 0


input = "0-1"
output = myAtoi(input)

print(output)
