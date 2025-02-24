"""
1980: Find Unique Binary String 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""

import itertools


def findUniqueBinaryString(nums):
    binary = ["01"]
    n = len(nums[0])

    array = []
    for i in itertools.product(*binary, repeat=n):
        combined = "".join(i)
        array.append(combined)

    not_in_array = []
    for i in array:
        if i not in nums:
            not_in_array.append(i)

    return not_in_array


nums = ["01", "10"]
output = findUniqueBinaryString(nums)
print("output:", output)
