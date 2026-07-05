#Search in Rotated Sorted Array


n = int(input())
nums = list(map(int, input().split()))
target = int(input())


left = 0
right = n - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break

    # Left half is sorted
    if nums[left] <= nums[mid]:

        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half is sorted
    else:

        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

else:
    print(-1)
