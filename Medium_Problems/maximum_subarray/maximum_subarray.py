def max_subarray(nums):
    # Initialize variables for maximum subarray sum (maxSub) and current subarray sum (curSum)
    maxSub = nums[0]  # Initialize maxSub with the first element of the input list
    curSum = 0  # Initialize curSum as 0

    # Iterate through the elements in the input list 'nums'
    for n in nums:
        # Check if the current subarray sum (curSum) is negative
        if curSum < 0:
            curSum = 0  # Reset curSum to 0 if it's negative

        # Add the current element 'n' to the current subarray sum (curSum)
        curSum += n

        # Update the maximum subarray sum (maxSub) by taking the maximum of maxSub and curSum
        maxSub = max(maxSub, curSum)

    # Return the maximum subarray sum (maxSub)
    return maxSub

