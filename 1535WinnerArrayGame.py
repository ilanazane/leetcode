# 1535. Find the Winner of an Array Game

# Testcases 

# arr = [2,1,3,5,4,6,7]
# k = 2
# output: 5

# arr = [3,2,1]
# k = 10
# output: 3 

# arr = [1,25,35,42,68,70]
# k = 1 
# output: 25 

def getWinner(arr:list[int],k:int)->int:

    current_winner = arr[0]
    points = 0 

    for i in range(1,len(arr)):
        if arr[i] > current_winner: 
            current_winner = arr[i]
            points = 1
        else: 
            points +=1 

        if k == points: 
            return current_winner 

    




  
    





