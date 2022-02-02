#PYTHON PROGRAM TO SWAP 2 NUMBERS

num1 = int(input('Enter the 1st number'))
num2 = int(input('Enter the 2nd number'))

#swapping by creating a temporary varaible
temp = num1
num1 = num2
num2 =  temp
print('The swapped value of 1st number is {}'.format(num1))
print('The swapped value of 2nd number is {}'.format(num2))