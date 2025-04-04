

# BRUTE FORCE SOLUTION 
# this is O(n^3) because of the three nested for loops 

def minimumSelfBruteForce(nums:list[int]) -> int:

    sums = []

    for i in range(len(nums)): 
        for j in range(len(nums)): 
            for k in range(len(nums)): 

                total = 0 

                indexi = nums[i]
                indexj = nums[j]
                indexk = nums[k]

                if (indexi < indexj and indexk < indexj) and (i<j<k): 
                    total = indexi + indexj + indexk 
                    sums.append(total)
    if sums: 
        return min(sums)
    else: 
        return -1 

    

# OPTIMIZED SOLUTION 
# this is O(n) because of the three individual for loops ( O(3n) = O(n) ) 

def minimumSelfOptimized(nums:list[int]) -> int:

    n = len(nums)
   
    # find left min 
    minimum_i = float("inf")
    left_minimum = [0]*n

    for i in range(len(nums)):
        minimum_i = min(minimum_i,nums[i])
        left_minimum[i] = minimum_i 
    # print('left',left_minimum)

    # find right min 
    minimum_k = float("inf")
    right_minimum = [0]*n 

    for k in range(n-1,-1,-1):
        minimum_k = min(minimum_k,nums[k])
        right_minimum[k] = minimum_k

    # print('right',right_minimum)

    # find middle 
    minimum_j = float("inf")

    for j in range(1,n-1):

        if nums[j] > left_minimum[j] and nums[j] > right_minimum[j]: 
            total_sum = nums[j] + left_minimum[j]+ right_minimum[j]
            minimum_j = min(minimum_j,total_sum)

    if minimum_j != float("inf"): 
        return minimum_j
    else: 
        return -1


# TEST CASES 

nums = [8,6,1,5,3] # 9 
# nums = [5,4,8,7,10,2] # 13
# nums = [6,5,4,3,4,5] # -1 
# nums = [5,3,2,4,1,6,7,8] #7 

print('output: ', minimumSelfOptimized(nums))

