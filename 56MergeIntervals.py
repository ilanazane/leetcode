def mergedIntervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    :description: Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the non-overlapping
    intervals that cover all the intervals in the input.

    :input: list of intervals
    :output: list of merged intervals

    Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    """
    # sort in increasing order based on 0th index
    intervals = sorted(intervals)

    merged = []

    for interval in intervals:

        # if merged is empty or there is no overlap
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # if there is overlap
            if interval[0] <= merged[-1][1] and interval[1] > merged[-1][0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# print("output: ", mergedIntervals(intervals))


import unittest


class Testing(unittest.TestCase):

    def test_mergedIntervals(self):
        self.assertEqual(
            mergedIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(
            mergedIntervals([[1, 4], [4, 5]]),
            [[1, 5]],
        )
        self.assertEqual(
            mergedIntervals([[1, 3]]),
            [[1, 3]],
        )
        self.assertEqual(
            mergedIntervals([[1, 4], [0, 4]]),
            [[0, 4]],
        )
        self.assertEqual(
            mergedIntervals([[1, 4], [0, 1]]),
            [[0, 4]],
        )
        self.assertEqual(
            mergedIntervals([[1, 4], [2, 3]]),
            [[1, 4]],
        )


if __name__ == "__main__":
    unittest.main()
