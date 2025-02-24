### ACCEPTED ###

import numpy as np 

nums1 = [1,2]
nums2 = [3,4]

# merge array 
merged = np.append(nums1,nums2)
sorted = np.sort(merged)


# find median
median = float(np.median(sorted))
print(median)


