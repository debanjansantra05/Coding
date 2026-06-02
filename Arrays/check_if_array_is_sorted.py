# Check if array is sorted

n = int(input("Enter the no. of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

is_sorted = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Not Sorted")
