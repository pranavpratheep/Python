# Python Program to check Palindrome or not

word = input("Enter a Character : ")
word = word.casefold()

# reverse the string
rev_str = reversed(word)

# check if the string is equal to its reverse
if list(word) == list(rev_str):
    print("It is a Palindrome. ")
else:
    print("It is not a Palindrome. ")
