#Find majority element (>N/2)

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

count = 0
candidate = None

# Boyer-Moore Voting Algorithm
for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

# Verification
if arr.count(candidate) > n // 2:
    print(candidate)
else:
    print(-1)
