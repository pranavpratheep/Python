#Python Program to swap 2 variables
x = input("Enter a value for X :")
y = input("Enter a values for Y:")

#create a temporary variable and swap the values
temp = x
x = y
y = temp

#printing values
print('The value of X after swapping :{}'.format(x))
print('The value of Y after swapping :{}'.format(y))