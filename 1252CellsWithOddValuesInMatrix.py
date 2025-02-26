"""

1252. Cells with Odd Values in a Matrix 

Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

"""

import numpy as np


def oddCells(m: int, n: int, indices: list[list[int]]) -> int:

    # create m x n matrix
    input = np.array([[0] * n] * m)

    for i in range(len(indices)):
        # increment row
        step = 0
        rows = indices[i][step]
        input[rows, :] += 1

        # increment column
        step += 1
        cols = indices[i][step]
        input[:, cols] += 1

    # count all odd numbers in the matrix
    rows = len(input)
    cols = len(input[0])

    odd_counter = 0

    for i in range(rows):
        for j in range(cols):
            # check if odd
            if input[i][j] % 2 != 0:
                odd_counter += 1

    return odd_counter


m = 2
n = 3
indices = [[0, 1], [1, 1]]

print("output: ", oddCells(m, n, indices))
