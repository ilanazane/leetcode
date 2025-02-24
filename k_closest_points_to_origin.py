# 973 
# COMPLETED

import numpy as np 
import heapq

points = [[3,3],[5,-1],[-2,4]]
k = 2


def k_closest_points( points,k):

    min_heap = [] 

    for (x,y) in points:
        distance = x**2 + y**2
        min_heap.append((distance,[x,y]))

    heapq.heapify(min_heap)

    k_closest_points = []

    for i in range (k):
        k_closest_points.append(heapq.heappop(min_heap)[1])

    return True 

    
x = k_closest_points(points,k)
print(x)