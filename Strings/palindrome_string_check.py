#Palindrome string check

s = input("Input a string from the user: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
