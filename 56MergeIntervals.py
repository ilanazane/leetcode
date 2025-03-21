"""
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


intervals[i] = [starti, endi]
"""

char_set = []
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[1, 3]]
# intervals = [[1, 4], [5, 6]]

merged = []

for interval in intervals:
    # If merged list is empty or no overlap
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
        print(merged)
    else:
        # Merge overlapping intervals
        merged[-1][1] = max(merged[-1][1], interval[1])
print(merged)
