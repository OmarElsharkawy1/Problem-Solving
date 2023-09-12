def plusOne(digits):
    for i in range(len(digits)-1, -1,-1): # Iterate over the digits in reverse order
        if digits[i] == 9: # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        else: # If the digit is not 9, add one to it and return the updated list
            digits[i] += 1
            return digits
    return [1] + digits # If all digits were 9, add a new leading 1 and return the updated list
