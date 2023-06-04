def find_duplicates(nums):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    duplicates = []
    for num, freq in freq_dict.items():
        if freq > 1:
            duplicates.append(num)

    return duplicates

print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))
