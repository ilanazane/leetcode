"""
Shortest Subarray with Sum at Least K

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3

Input: nums = [2,2,-1,5], k = 3
Output: 3

"""


def shortestSubarray(nums: list[int], k: int) -> int:
    subarray_sum = []

    for i in range(len(nums)):
        start = i
        end = len(nums)

        while start != end:
            x = nums[start:end]
            if sum(x) >= k:
                subarray_sum.append(len(x))

            end -= 1
    try:
        return min(subarray_sum)
    except:
        return -1


nums = [2, -1, 2]
k = 3

# print("output", shortestSubarray(nums, k))


# optimized approach:
from collections import deque


def shortestSubarrayOptimized(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)

    # Compute prefix sums
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    min_length = float("inf")
    dq = deque()  # Stores indices of prefix_sum

    for i in range(n + 1):
        # Check if there exists a valid subarray
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            min_length = min(min_length, i - dq.popleft())

        # Maintain increasing order in the deque
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()

        dq.append(i)

    return min_length if min_length != float("inf") else -1
