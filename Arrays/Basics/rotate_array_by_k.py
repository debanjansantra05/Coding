#Rotate array by K (right rotation)

n = int(input("Enter no. of elements: "))

arr = list(map(int,input("Enter the elements using space: ").split()))

k = int(input("Enter the value of k: "))

k = k%n

rotated = arr[-k:] + arr[:-k]           #rotated = arr[-k:] + arr[:-k] (for left rotation)

print(*rotated)
