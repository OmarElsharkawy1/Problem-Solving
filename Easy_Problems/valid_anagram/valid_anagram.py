def is_anagram(s, t):
    # Check if the lengths of the two input strings are not equal
    if len(s) != len(t):
        return False

    # Iterate through the unique characters in string 's'
    for char in set(s):
        # Check if the count of the current character in 's' is not equal to its count in 't'
        if s.count(char) != t.count(char):
            return False

    # If all characters in 's' have the same count in 't', return True (they are anagrams)
    return True
