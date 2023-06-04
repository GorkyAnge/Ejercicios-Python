def find_max_min(myList):
    if not myList:
        return None

    max_val = float('-inf')
    min_val = float('inf')

    for num in myList:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return (max_val, min_val)


print(find_max_min([5, 3, 8, 1, 6, 9]))   
