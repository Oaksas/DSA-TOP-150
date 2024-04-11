def removeDuplicates(self, nums: List[int]) -> int:
    count = 0
    x = {x: 0 for x in nums}
    removeIndexes = []
    for i in range(len(nums)):
        if x[nums[i]] < 2:
            x[nums[i]] += 1
            count += 1
        else:
            removeIndexes.append(i)

    nums[:] = [nums[i] for i in range(len(nums)) if i not in removeIndexes]
    return count
