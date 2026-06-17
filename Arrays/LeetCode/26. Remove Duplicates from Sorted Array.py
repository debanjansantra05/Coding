#Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1  # Pointer for unique elements

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


# Input
nums = list(map(int, input().split()))

k = removeDuplicates(nums)

print(k)
print(nums[:k])
