def min_length_after_removal(s):
    # Initialize an empty stack to hold characters
    stack = []

    # Iterate through each character in the input string 's'
    for c in s:
        # Push the current character onto the stack
        stack.append(c)

        # Check if there are at least two characters in the stack
        if len(stack) > 1:
            # Check if the last two characters in the stack form either 'AB' or 'CD'
            if ''.join(stack[-2:]) in ['AB', 'CD']:
                # If they do, pop both characters from the stack
                stack.pop()
                stack.pop()

    # The length of the stack after processing is the minimum length
    # of the string after removing pairs of 'AB' or 'CD'
    return len(stack)

# Example usage:
input_string = "ABCDAB"
result = min_length_after_removal(input_string)
print("Minimum length after removal:", result)
