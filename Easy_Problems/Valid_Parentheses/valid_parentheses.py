
def isValid(s: str):
    possible_str = {'(': ')', '{': '}', '[' : ']'}
    openings = []

    if len(s) % 2 != 0:
        return False
    
    for symbol in s:
        if symbol in possible_str.keys():
            openings.append(symbol)
        elif openings == [] or symbol != possible_str[openings.pop()]:
            return False
    
    return openings == []
