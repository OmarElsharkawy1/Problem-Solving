def max_profit(prices):
    # Initialize variables for left pointer (l), right pointer (r), and maximum profit (maxP).
    l, r, maxP = 0, 0, 0
    
    # Iterate through the list 'prices' using the right pointer (r).
    while r < len(prices):
        # Check if the price at the left pointer (l) is less than the price at the right pointer (r).
        if prices[l] < prices[r]:
            # Calculate the profit by subtracting the price at l from the price at r.
            profit = prices[r] - prices[l]
            
            # Update the maximum profit (maxP) if the current profit is greater.
            maxP = max(maxP, profit)
        else:
            # If the price at l is greater than or equal to the price at r, move the left pointer (l) to r.
            l = r
        
        # Move the right pointer (r) to the next day.
        r += 1
    
    # Return the maximum profit obtained.
    return maxP
