def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)
    