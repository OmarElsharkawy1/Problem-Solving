def isValid(s: str):
    possible_str = {'(': ')', '{': '}', '[' : ']'}  # Define a dictionary of possible opening and closing symbols
    openings = []  # Initialize an empty list to store opening symbols

    if len(s) % 2 != 0:
        return False  # If the length of the input string is odd, it cannot be valid

    for symbol in s:
        # Iterate through each character in the input string
        if symbol in possible_str.keys():
            # If the symbol is an opening symbol, add it to the 'openings' list
            openings.append(symbol)
        elif openings == [] or symbol != possible_str[openings.pop()]:
            # If the symbol is a closing symbol, check if it matches the corresponding opening symbol
            # If the 'openings' list is empty or the current symbol does not match the expected closing symbol
            return False  # Return False, indicating an invalid string

    return openings == []  # Return True if all opening symbols have been closed, otherwise return False