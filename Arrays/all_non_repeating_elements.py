#All non-repeating elements

n = int(input("Enter the no. of elements: "))

arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

found = False

print("Non-repeating elements are:")

for num in arr:
    if freq[num] == 1:
        print(num, end=" ")
        found = True

if not found:
    print(-1)
