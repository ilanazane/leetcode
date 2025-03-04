def removeCoveredIntervals(intervals: list[list[int]]) -> int:
    """
    :params: 2D list of ints
    :returns: int that is len of remaining list

    Example 1:

    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

    Example 2:

    Input: intervals = [[1,4],[2,3]]
    Output: 1

    """

    for i in range(len(intervals) - 1):

        # get first interval
        first = intervals[i]

        # get second interval
        second = intervals[i + 1]

        # compare intervals

        # (a,b) is covered by (c,d) if c<=a and b<=d
        if (second[0] <= first[0]) and (first[1] <= second[1]):
            intervals.remove(first)
        # (a,b) is covered by (c,d) if c>=a and b>=d
        elif (second[0] >= first[0]) and (first[1] >= second[1]):
            intervals.remove(second)

    return len(intervals)


intervals = [[1, 4], [3, 6], [2, 8]]
# intervals = [[1, 4], [2, 3]]

print("output: ", removeCoveredIntervals(intervals))
