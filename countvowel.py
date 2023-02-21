# Python Program to count the number of each vowel in string

vowels = 'aeiou'
character = input("Enter the Character : ")
character = character.casefold()

count = {}.fromkeys(vowels,0)

# count the vowels
for char in character:
    if char in count:
        count[char] += 1
        print(count)