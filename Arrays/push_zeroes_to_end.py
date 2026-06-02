# Read input
n = int(input())
arr = list(map(int, input().split()))

# Position to place non-zero elements
index = 0

# Move non-zero elements forward
for i in range(n):
    if arr[i] != 0:
        arr[index] = arr[i]
        index += 1

# Fill remaining positions with 0
while index < n:
    arr[index] = 0
    index += 1

# Print result
print(*arr)
