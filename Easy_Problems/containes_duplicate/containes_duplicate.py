def contains_duplicate(nums):
    # Create an empty set to store unique numbers
    num_set = set()

    # Iterate through the input list 'nums'
    for num in nums:
        # Check if the current number is already in the set
        if num in num_set:
            # If it is, a duplicate has been found, so return True
            return True
        else:
            # If not, add the current number to the set
            num_set.add(num)

    # If the loop completes without finding any duplicates, return False
    return False
