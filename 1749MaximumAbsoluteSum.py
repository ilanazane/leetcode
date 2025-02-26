"""
Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
"""


def maxAbsoluteSum(nums: list[int]) -> int:

    sums = []
    for i in range(len(nums)):
        # print(nums[i])
        start = i
        end = len(nums)

        while start != end:
            sums.append(abs(sum(nums[start:end])))

            end -= 1

    return max(sums)


nums = [2, -5, 1, -4, 3, -2]
print(maxAbsoluteSum(nums))
