"""
zig-zag conversion 
"""

s = "PAYPALISHIRING"
numRows = 4

rows = [""] * numRows
print(rows)

index = 0
step = 1

for char in s:
    rows[index] += char

    # at top of table
    if index == 0:
        # move down
        step = 1

    # at bottom of table
    if index == numRows - 1:
        # move up
        step = -1

    # increase or decrease index
    index += step

print("".join(rows))
