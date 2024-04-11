def twoSum(nums, target):
    start = 0
    end = len(nums)-1
    while start < end:
        if nums[start]+nums[end] == target:
            return [start, end]
        elif nums[start]+nums[end] > target:
            end -= 1
        else:
            start += 1
    return -1


print(twoSum([2, 7, 11, 15], 9))
