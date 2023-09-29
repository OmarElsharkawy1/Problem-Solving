def max_product(nums):
    # Check if the input list 'nums' is empty.
    if len(nums) < 1:
        return 0

    # Initialize variables to track maximum product, current maximum, and current minimum.
    _max = cur_max = cur_min = nums[0]

    # Iterate through the input list 'nums' starting from the second element.
    for num in nums[1:]:
        # Store the current maximum value in 'tmp' for use in updating 'cur_min'.
        tmp = cur_max

        # Update 'cur_max' by taking the maximum of three values: 'num', 'num * cur_max', and 'num * cur_min'.
        cur_max = max(num, num * cur_max, num * cur_min)

        # Update 'cur_min' by taking the minimum of three values: 'num', 'num * tmp', and 'num * cur_min'.
        cur_min = min(num, num * tmp, num * cur_min)

        # Update the overall maximum product '_max' by taking the maximum of '_max' and 'cur_max'.
        _max = max(_max, cur_max)

    # Return the maximum product calculated.
    return _max