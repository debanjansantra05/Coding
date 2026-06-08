#Count frequency of elements

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, "->", freq[key])
