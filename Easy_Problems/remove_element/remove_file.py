def removeElement( nums, val) -> int:
    """
    Remove all occurrences of a given value from a list.

    Args:
        nums (List[int]): The input list containing integers.
        val (int): The value to be removed from the list.

    Returns:
        int: The length of the modified list after removing the value.

    Algorithm:
        - Initialize a variable k to keep track of the index for inserting non-val elements.
        - Iterate through the list using a for loop.
        - If the current element is not equal to val, assign it to nums[k] and increment k by 1.
        - After iterating through the entire list, the value of k represents the length of the modified list.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k