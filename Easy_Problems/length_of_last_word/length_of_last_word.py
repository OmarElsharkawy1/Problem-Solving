def lengthOfLastWord(self, s):
    """
    Calculate the length of the last word in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the last word.

    Algorithm:
        1. Initialize a pointer `i` to the last index of the string `s` and a variable `length` to 0.

        2. Iterate backwards from index `i` until a non-space character is encountered.
           - Decrement `i` by 1 in each iteration.
           - This loop ensures that any trailing spaces at the end of the string are ignored.

        3. Iterate backwards from index `i` until a space character is encountered or `i` becomes less than 0.
           - Increment `length` by 1 in each iteration to count the characters of the last word.
           - Decrement `i` by 1 in each iteration.

        4. Return the value of `length`, which represents the length of the last word.

    Complexity Analysis:
        - Time Complexity: O(n), where n is the length of the input string `s`.
          The function iterates through the string twice, once to skip trailing spaces and once to count the characters of the last word.

        - Space Complexity: O(1), the function uses a constant amount of additional memory to store the variables `i` and `length`.
    """
    i, length = len(s) - 1, 0

    # Skip trailing spaces
    while s[i] == ' ':
        i -= 1

    # Count characters of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length