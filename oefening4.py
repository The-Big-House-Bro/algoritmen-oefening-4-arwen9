def countTargetPairs(nums, target):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1

    return count

nums = [-1, 1, 2, 3, 1]
target = 2
print(countTargetPairs(nums, target))


nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2
print(countTargetPairs(nums, target))

