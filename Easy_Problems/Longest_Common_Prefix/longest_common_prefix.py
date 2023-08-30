#A function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string

def longestCommonPrefix(strs):
    result = ''  # Initialize an empty string to store the longest common prefix
    strs.sort()  # Sort the list of strings in lexicographical order

    first = strs[0]  # Assign the first string in the sorted list to 'first'
    last = strs[len(strs) - 1]  # Assign the last string in the sorted list to 'last'

    for i in range(len(first)):
        # Iterate through the characters of the 'first' string
        if first[i] != last[i]:
            # If the character at index 'i' in 'first' is not equal to the character at index 'i' in 'last'
            break  # Break out of the loop since the common prefix ends at this point
        result = result + first[i]  # Append the character to the 'result' string

    if result == '':
        # If the 'result' string is empty, there is no common prefix among the strings
        return ''  # Return an empty string
    else:
        # If the 'result' string is not empty, return the 'result' string, which represents the longest common prefix
        return result