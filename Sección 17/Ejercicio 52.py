def item_in_common(list1, list2):
    item_dict = {}
    for item in list1:
        item_dict[item] = True
    for item in list2:
        if item in item_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
