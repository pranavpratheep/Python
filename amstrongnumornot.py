#Python program to check if the number provided by the user is an Armstrong number or not
num = int(input("Enter a number :"))
sum = 0

#find the sum of the cube of each digit
temp = num
while temp>0:
    digit = temp%10
    sum += digit ** 3
    temp //= 10
#display the digit
if num == sum:
    print(num,"is an Amstrong Number.")
else:
    print(num,"is not Amstrong Number.")