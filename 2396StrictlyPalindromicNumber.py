# check base from 2 to n - 2
def convertToBinary(n: int) -> list[str]:
    # get end range
    b = n - 2

    nums_list = []

    for i in range(2, b + 1):
        nums = ""
        input = n

        # calculate binary strings
        while input:
            input, r = divmod(input, i)
            nums += str(r)
        nums_list.append("".join(reversed(nums)))

    return nums_list


# check if palindrome
def isStrictlyPalindrome(n: int) -> bool:

    binary_list = convertToBinary(n)

    reversed_binary_list = []

    # reverse every binary number
    for i in binary_list:
        reverse_str = "".join(reversed(i))
        reversed_binary_list.append(reverse_str)

    # if strictly palindromic both lists will be equal
    if reversed_binary_list == binary_list:
        return True
    # any differences means it is not strictly palindromic
    else:
        return False


n = 4
print("output: ", isStrictlyPalindrome(n))
