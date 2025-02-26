def numOfSubarrays(arr: list) -> int:
    """
    return the number of subarrays with an odd sum

    :param list: a list of numbers
    :returns int: a counter of subarrays with odd sum


    Example 1:

    Input: arr = [1,3,5]
    Output: 4
    Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
    All sub-arrays sum are [1,4,9,3,8,5].
    Odd sums are [1,9,3,5] so the answer is 4.
    """
    counter = 0

    for i in range(len(arr)):
        start = i
        end = len(arr)

        while start != end:
            # get the subarray
            interval = arr[start:end]

            # get the sum of the subarray
            sum_of_interval = sum(interval)

            # check if sum is odd
            if sum_of_interval % 2 != 0:
                counter += 1

            # decrement end pointer
            end -= 1

    return counter


input = [1, 2, 3, 4, 5, 6, 7]
print("output: ", numOfSubarrays(input))
