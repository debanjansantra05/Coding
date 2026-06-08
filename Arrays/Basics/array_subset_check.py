#Array subset check

n = int(input("Enter the number of elements: "))
A = list(map(int, input("Enter the array elements separated by spaces: ").split()))

m = int(input("Enter the number of elements: "))
B = list(map(int, input("Enter the array elements separated by spaces: ").split()))

s = set(A)

flag = True

for num in B:
    if num not in s:
        flag = False
        break

print("Yes" if flag else "No")
