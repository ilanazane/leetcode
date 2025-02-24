""" 
Best Team With No Conflicts 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Example 3:


Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 

"""

# scores = [1, 3, 5, 10, 15]
# ages = [1, 2, 3, 4, 5]

scores = [4, 5, 6, 5]
ages = [2, 1, 2, 1]

# scores = [1, 2, 3, 5]
# ages = [8, 9, 10, 1]

players = sorted(zip(ages, scores), key=lambda x: (x[0], x[1]))
print(players)

n = len(players)
print(n)
dp = [score for _, score in players]
print(dp)


for i in range(n):
    for j in range(i):
        print(i, j)
        print(dp[i])
        print(dp[j])
        print(players[i][1])
        print(dp)
        if players[i][1] >= players[j][1]:
            dp[i] = max(dp[i], dp[j] + players[i][1])
            print(dp)
