def addBinary(a, b):
    res = ''  # Initialize an empty string to store the result
    carry = 0  # Initialize the carry variable to 0
    a, b = a[::-1], b[::-1]  # Reverse both input strings

    # Iterate over the digits of the longer string from right to left
    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord('0') if i < len(a) else 0  # Get the current digit of 'a'. If the index exceeds the length, set the digit to 0
        digitB = ord(b[i]) - ord('0') if i < len(b) else 0  # Get the current digit of 'b'. If the index exceeds the length, set the digit to 0

        total = digitA + digitB + carry  # Calculate the sum of the digits and the carry
        char = str(total % 2)  # Calculate the value of the current digit in the result string
        res = char + res  # Append the digit to the left side of the result string
        carry = total // 2  # Update the carry

    if carry:  # If there is a remaining carry
        res = '1' + res  # Append '1' to the left side of the result string
    return res  # Return the result string