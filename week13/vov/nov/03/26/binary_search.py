def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if items [mid] == target:
            return mid
        elif items [mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#example usage
values = [10,20,30,40,50,60,70]
target = 40
result = binary_search(numbers, target)
if result != -1:
    print(f"target found at index {result}")
else:
    print("target not found")
    