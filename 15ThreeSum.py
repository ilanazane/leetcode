def ThreeSum(nums):

    # sort values

    sorted_nums = sorted(nums)

    triplets = []

    for i in range(len(sorted_nums) - 2):

        # initiate pointers
        left = i + 1
        right = len(sorted_nums) - 1

        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            # print(total)

            if total < 0:  # sum too small, increase left pointer
                left += 1
            elif total > 0:  # sum too big, decrease right pointer
                right -= 1
            else:  # triplet found
                triplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                left += 1  # increase left
                right -= 1  # decrease right

    x = {tuple(row) for row in triplets}
    return list(x)


input = [-1, 0, 1, 2, -1, -4]
output = ThreeSum(input)
print(output)
