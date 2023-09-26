def three_sum(nums):
    # Initialize an empty list 'res' to store unique triplets that sum to zero.
    res = []

    # Sort the input list 'nums' in ascending order.
    nums.sort()

    # Iterate through 'nums' using enumeration.
    for i, val in enumerate(nums):
        # Skip duplicate values to avoid duplicate triplets.
        if i > 0 and val == nums[i - 1]:
            continue

        # Initialize left (l) and right (r) pointers.
        l = i + 1
        r = len(nums) - 1

        # Explore the two-pointer approach.
        while l < r:
            threesum = val + nums[l] + nums[r]

            # If the sum of the triplet is greater than zero, move the right pointer (r) leftward.
            if threesum > 0:
                r -= 1

            # If the sum of the triplet is less than zero, move the left pointer (l) rightward.
            elif threesum < 0:
                l += 1

            # If the sum of the triplet is zero, append it to 'res' and update pointers.
            else:
                res.append([val, nums[l], nums[r]])
                l += 1

                # Skip duplicate values to avoid duplicate triplets.
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    # Return the list of unique triplets that sum to zero.
    return res