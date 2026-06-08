#Remove duplicates from array

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print("Array after removing duplicates:")
print(*result)
