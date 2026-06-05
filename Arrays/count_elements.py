#Count elements > all previous

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

count = 1
max_so_far = arr[0]

for i in range(1, n):
    if arr[i] > max_so_far:
        count += 1
        max_so_far = arr[i]

print(count)
