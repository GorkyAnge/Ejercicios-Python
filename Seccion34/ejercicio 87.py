def remove_element(nums, val):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == val:
            nums[i] = nums[j]
            nums.pop()
            j -= 1
        else:
            i += 1

    return len(nums)


# Test case 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
new_length1 = remove_element(nums1, val1)
print("Test case 1: Modified array:", nums1, "\nNew length:", new_length1)

# Test case 2
nums2 = [1, 2, 3, 4, 5, 6]
val2 = 6
new_length2 = remove_element(nums2, val2)
print("Test case 2: Modified array:", nums2, "\nNew length:", new_length2)

# Test case 3
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
new_length3 = remove_element(nums3, val3)
print("Test case 3: Modified array:", nums3, "\nNew length:", new_length3)

# Test case 4
nums4 = []
val4 = 1
new_length4 = remove_element(nums4, val4)
print("Test case 4: Modified array:", nums4, "\nNew length:", new_length4)

# Test case 5
nums5 = [1, 1, 1, 1, 1]
val5 = 1
new_length5 = remove_element(nums5, val5)
print("Test case 5: Modified array:", nums5, "\nNew length:", new_length5)
