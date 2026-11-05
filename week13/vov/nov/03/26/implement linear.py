def linear_search(items,target):
    for index,value in enumerate(items):
        if value == target:  
        return index
    
     return -1

values =([10,4,12,8]
print(linear_search(values,12)) #2
print(linear_search(values,5))  #-1

     