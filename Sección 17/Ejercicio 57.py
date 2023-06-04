def subarray_sum(nums, target):
    sum_dict = {0: -1}
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - target in sum_dict:
            return [sum_dict[curr_sum - target] + 1, i]
        sum_dict[curr_sum] = i
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))
