word = input("Enter a word: ")

def pal(word):
    temp = word
    if (word[::-1] == temp):
        print("palindrome")
    else:
        print("not palindrome")

pal(word)