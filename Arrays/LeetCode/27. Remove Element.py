#Remove Element

def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

nums = list(map(int, input().split()))
val = int(input())

k = removeElement(nums, val)

print(k)
print(*nums[:k])
