points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
distances = [] 
# minimum cost for the points, no repeating points 


from itertools import product,permutations

def manhattan_distance(starting_points,points_list):
    distance =[] 
    for i in range(len(points_list)): 
        if starting_point!= points_list[i]:
            distance.append([abs(starting_points[0]- points_list[i][0]) + abs(starting_points[1]-points_list[i][1]),starting_point,points[i]])
    return distance
all_distances = [] 
for i in range(len(points)): 

    starting_point = points[i]
    final_distance = min(manhattan_distance(starting_point,points))
    all_distances.append(final_distance)

edges = sorted(all_distances)


unique_edges = {}
total_distance = 0 

for distance, x, y in edges: 
    edge_key = tuple(sorted([tuple(x),tuple(y)]))
    print(edge_key)

    if edge_key not in unique_edges: 
        unique_edges[edge_key] = distance 
        total_distance += distance

print(unique_edges)
print(total_distance)
