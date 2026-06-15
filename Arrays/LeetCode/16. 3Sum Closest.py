#3Sum Closest

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()

closest_sum = nums[0] + nums[1] + nums[2]

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            print(current_sum)
            exit()

print(closest_sum)
