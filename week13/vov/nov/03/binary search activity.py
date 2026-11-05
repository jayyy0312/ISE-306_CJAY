data =[2,6,10,14,18,22,26]
target = 18

low, high = 0, len(data) - 1
while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
        print(low, mid, data[mid])
        print("found",mid)
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
        