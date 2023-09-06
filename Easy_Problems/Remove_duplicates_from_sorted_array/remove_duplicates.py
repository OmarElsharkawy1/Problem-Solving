def removeDuplicates(self, nums):
    uniquePointer = 1  # Initialize a pointer to track the position of the unique elements
    for i in range(1, len(nums)):
        if nums[i] != nums[uniquePointer - 1]:
            # If the current element is different from the previous unique element
            nums[uniquePointer] = nums[i]  # Move the current element to the next unique position
            uniquePointer += 1  # Increment the unique pointer to the next position
    return uniquePointer