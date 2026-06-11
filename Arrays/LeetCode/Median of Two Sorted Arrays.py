#Median of Two Sorted Arrays

n1 = int(input())
nums1 = list(map(int, input().split()))

n2 = int(input())
nums2 = list(map(int, input().split()))

arr = nums1 + nums2
arr.sort()

n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print("{:.5f}".format(median))
