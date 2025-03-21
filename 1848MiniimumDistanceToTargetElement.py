"""
Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
"""

# nums = [1,2,3,4,5]
# target = 5
# start = 3

# nums = [1]
# target = 1
# start = 0

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0

def minimumDistanceToTarget(nums:list[int],target:int,start:int)->int:

    abs_values = []
    for i in range(len(nums)):
        # find target
        if nums[i] == target:
            print('yes',i)
            # get absolute values 
            ab = abs(i-start)
            abs_values.append(ab)

    return min(abs_values)

print('output: ',minimumDistanceToTarget(nums,target,start))


