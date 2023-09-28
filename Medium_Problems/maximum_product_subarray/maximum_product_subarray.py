def maxProduct(nums):
    if len(nums) < 1:
        return 0
    _max, cur_max, cur_min = 1
    for num in nums[1:]:
        tmp = cur_max
        cur_max = max(num, num*cur_max, num*cur_min)
        cur_min = min(num, num*tmp, num*cur_min)
        _max = max(num, cur_max, cur_min)

    return _max