#Longest Common Prefix

n = int(input())

arr = []
for i in range(n):
    arr.append(input())

prefix = arr[0]

for i in range(1, n):
    while arr[i].find(prefix) != 0:
        prefix = prefix[:-1]

        if prefix == "":
            print("")
            exit()

print(prefix)
