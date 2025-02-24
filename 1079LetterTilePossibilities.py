import itertools

"""
Input: tiles = "AAB"
Output: 8
"""


def letterTilePossibilities(input):
    # create an array that holds sets of permutations
    new_vals = []
    for i in range(1, len(input) + 1):
        # append unique permutations
        new_vals.append(set(list(itertools.permutations(input, i))))

    # create new set
    combined_set = set()

    for s in new_vals:
        # combine all of the sets from the array
        combined_set.update(s)

    # get the number of unique sets
    length = len(combined_set)
    return length


input = "AAABBC"
output = letterTilePossibilities(input)

print(output)
