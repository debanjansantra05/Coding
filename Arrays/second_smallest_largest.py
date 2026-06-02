#Second smallest & largest

n = int(input("Enter the no. of elements: "))

arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

unique_arr = sorted(set(arr))

if len(unique_arr) < 2:
    print("Not Possible")
else:
    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]

    print(second_smallest, second_largest)
