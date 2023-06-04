def longest_consecutive_sequence(nums):
    # Create a set of all numbers in the array
    num_set = set(nums)
    max_length = 0

    # Iterate through each number in the array
    for num in nums:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Check the next consecutive numbers in the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update the maximum length if necessary
            max_length = max(max_length, current_length)

    return max_length
