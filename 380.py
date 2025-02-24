#  380. Insert Delete GetRandom O(1)

# not tested or submitted, this code is based off of the one test case provided 

# potential issues: 
    # did not follow provided data structure with class 
    # RandomizedSet() just returns an empty list, a set is initialized and passed automatically 


import random

# convert string input into function 
def str_to_func(final_list, myset, expression, element):
    
    # insert 
    if expression == "insert": 
        if element not in (myset): 
            myset.add(element)
            final_list.append(True)
        else: 
            final_list.append(False)

    # remove
    if expression == "remove":
        if element in myset: 
            myset.remove(element)
            final_list.append(True)
        else: 
           final_list.append(False)
        
    # get random 
    if expression == "getRandom":
        mylist = list(myset)
        if mylist:
            random_element = random.choice(mylist)
            final_list.append(random_element)
        else: 
            final_list.append(False)

    # initialize randomized set 
    if expression == "RandomizedSet": 
        final_list.append([])
        
    return  final_list

commands = [ "RandomizedSet","insert", "remove", "insert","getRandom", "remove", "insert","getRandom"]
values = [[],[1], [2], [2], [], [1], [2], []]
final_list = [] 
myset = set()


# combine commands with corresponding values
for i in range(len(commands)):
    x = list(zip(commands,values))

for i in range(len(x)):
    function = str(x[i][0])

    # try to get values
    try:
        value = x[i][1][0]
    except: 
        value = 0 
    else:
        value = x[i][1][0]
    
    my_function = str_to_func(final_list, myset, function,value)

    result = my_function  


print(result)





