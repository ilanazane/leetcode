# valid sudoku


def sudoku(board: list[list["str"]]) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated

    :param 2D array:
    :returns bool:
    """
    import numpy as np

    new_board = np.array(board)

    for row in new_board:
        row_array = []
        for j in row:
            if j != ".":
                row_array.append(j)
        if len(row_array) != len(set(row_array)):
            return False

    for col in new_board.T:
        col_array = []
        for j in col:
            if j != ".":
                col_array.append(j)
        print(col_array)
        if len(col_array) != len(set(col_array)):
            return False

    return True


# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
output = sudoku(board)
print(output)
