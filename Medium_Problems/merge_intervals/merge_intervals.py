def merge(intervals):
    # Initialize an empty list 'output' to store the merged intervals.
    output = []

    # Sort the input intervals based on their start values in ascending order.
    for i in sorted(intervals, key=lambda i: i[0]):
        # Check if 'output' is not empty and the current interval overlaps with the last interval in 'output'.
        if output and i[0] <= output[-1][1]:
            # Merge the overlapping intervals by updating the end value of the last interval in 'output'.
            output[-1][1] = max(output[-1][1], i[1])
        else:
            # If there is no overlap, add the current interval to 'output'.
            output += i,

    # Return the merged intervals.
    return output