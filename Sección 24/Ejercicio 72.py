def insertion_sort(my_list):
    n = len(my_list)

    for i in range(1, n):
        temp = my_list[i]
        j = i - 1

        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1

        my_list[j + 1] = temp

    return my_list





print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

