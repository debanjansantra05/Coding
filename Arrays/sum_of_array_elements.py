#Sum of array elements

n = int(input("Enter the size of the array: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

total = sum(arr)

print("Sum of array elements =", total)
