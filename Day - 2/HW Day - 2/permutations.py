def permute(nums, temp=None, used=None):
    if temp is None:
        temp = []
    if used is None:
        used = [False] * len(nums)

    if len(temp) == len(nums):
        print(temp)
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        temp.append(nums[i])
        permute(nums, temp, used)
        temp.pop()
        used[i] = False

nums = [1, 2, 3]
permute(nums)
