def linear_search(items,target):
    for index, value in enumerate(items):
        if value == target:
            return index
        return-1

values = [9,4,13,7,16,2]
print(linear_search(values,17)) #4
print(linear_search(values,4))   #-1 
