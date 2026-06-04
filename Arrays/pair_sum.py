# Two-sum / pair sum

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the target sum: "))

seen = set()
found = False

for num in arr:
    complement = k - num

    if complement in seen:
        print(complement, num)
        found = True
        break

    seen.add(num)

if not found:
    print("No Pair Found")
