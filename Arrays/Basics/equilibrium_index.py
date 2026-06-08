#Find equilibrium index 

n = int(input("Enter the size of array: "))

arr = list(map(int, input("Enter array elements separated by space: ").split()))

total_sum = sum(arr)
left_sum = 0

for i in range(n):

    total_sum -= arr[i]

    if left_sum == total_sum:
        print("Equilibrium Index:", i)
        break

    left_sum += arr[i]

else:
    print("Equilibrium Index: -1")
