#Container With Most Water

n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1
max_area = 0

while left < right:
    width = right - left
    area = min(height[left], height[right]) * width

    if area > max_area:
        max_area = area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_area)
