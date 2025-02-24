"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
"""

import itertools


def product_no_repeats(input, n, k):

    # asterisk unpacks the list
    for combinations in itertools.product(*input, repeat=n):
        is_consecutive = False
        for i in range(len(combinations) - 1):
            # compare consecutive letters
            if combinations[i] == combinations[i + 1]:
                is_consecutive = True
                break
        if not is_consecutive:
            # if not consecutive then generate the combination
            yield combinations

    return combinations


input = ["a", "b", "c"]
n = 3
k = 9

# needs to be 2D array so that the entire list is considered
output = product_no_repeats([input], n, k)

final = []
for i in output:
    # output is generated only when it is called, which is why we cannot randomly access the values
    # if function creates output then it is shown.
    final.append(i)

print(len(final))
print(final[k - 1])
