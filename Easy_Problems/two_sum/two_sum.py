def two_sum(nums, target):
    # Create an empty dictionary to store the complement of numbers and their indices
    complement_dict = {}

    # Iterate through the list 'nums' along with their indices using enumerate
    for i, num in enumerate(nums):
        # Calculate the difference between the target and the current number
        diff = target - num

        # Check if the difference (complement) exists in the dictionary
        if diff in complement_dict:
            # If it does, return the indices of the two numbers that sum to the target
            return [complement_dict[diff], i]

        # Store the current number and its index in the dictionary
        complement_dict[num] = i
