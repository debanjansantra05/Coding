#Mean/median of array

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

mean = sum(arr) / n

arr.sort()

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print(f"Mean = {mean:.2f}")
print(f"Median = {median}")
