#Reverse words in sentence

sentence = input("Input a sentence from the user: ")

words = sentence.split()
reversed_words = words[::-1]

print(" ".join(reversed_words))
