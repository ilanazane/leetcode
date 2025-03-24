def minPathSum(grid: list[list[int]]) -> int:

    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):

            # skip the top left cell
            if i == 0 and j == 0:
                continue

            # check the first row
            elif i == 0:
                grid[i][j] += grid[i][j - 1]

            # check the fist column
            elif j == 0:
                grid[i][j] += grid[i - 1][j]

            # check inside the grid
            else:
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

    # find the bottom right cell
    return grid[-1][-1]


grid = [[1, 2, 3], [4, 5, 6]]
print("output:", minPathSum(grid))
