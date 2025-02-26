"""
Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. 
After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. 
The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
"""


def rangeSum(nums: list[int], n: int, left: int, right: int) -> int:
    """
    :description: 1508. Range Sum of Sorted Subarray Sums
    :params: nums,n,left,right
    :return: int
    """

    sum_sub_arrays = []

    for i in range(len(nums)):
        # left pointer
        start = i
        # right pointer
        end = len(nums)

        while start != end:
            # get sum of all subarrays
            sum_sub_arrays.append(sum(nums[start:end]))

            # decrement end pointer
            end -= 1

    # sort sums of subarrays
    sorted_array = sorted(sum_sub_arrays)

    # find the sum from left to right
    final_sum = sum(sorted_array[left - 1 : right])

    return final_sum


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 10
print("output:", rangeSum(nums, n, left, right))
