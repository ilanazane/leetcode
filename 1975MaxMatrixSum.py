matrix = [[1,-1],[-1,1]]
# matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]


def maxMatrixSum(matrix): 

    total = 0 
    negatives = 0 
    min_value = float("inf") 

    # assume that all values are positive - find total  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): 

            # find total absolute value
            total += abs(matrix[i][j])

            # count negative numbers in matrix 
            if matrix[i][j] < 0: 
                negatives += 1 

            # keep track of minimum absolute value
            min_value = min(min_value,abs(matrix[i][j]))

    # if even num of negatives, return total 
    if negatives % 2 == 0: 
        return total 
    # otherwise we need to keep one negative. subtract doubly accounted for min abs value
    else: 
        total = total - 2 * min_value
        return total


print('max sum: ',maxMatrixSum(matrix))