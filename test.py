def insertion_sort(nums):
    length = len(nums)
    for i in range(length, 0, -1):
        for j in range(i-1, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
