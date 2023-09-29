def search(nums, target):
    # Initialize left (l) and right (r) pointers.
    l = 0
    r = len(nums) - 1

    # Perform binary search while 'l' is less than or equal to 'r'.
    while l <= r:
        # Calculate the middle index.
        mid = (l + r) // 2

        # Check if the target value is equal to the middle element.
        if target == nums[mid]:
            return mid

        # Check if the left subarray (from 'l' to 'mid') is sorted.
        if nums[l] <= nums[mid]:
            # If the target is greater than the middle element or less than the leftmost element,
            # narrow the search to the right subarray.
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            # Otherwise, narrow the search to the left subarray.
            else:
                r = mid - 1
        # If the left subarray is not sorted, the right subarray must be sorted.
        else:
            # If the target is less than the middle element or greater than the rightmost element,
            # narrow the search to the left subarray.
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            # Otherwise, narrow the search to the right subarray.
            else:
                l = mid + 1

    # If the target is not found, return -1.
    return -1