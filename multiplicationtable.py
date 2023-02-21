#program to find Multiplication Table
num = int(input("Enter a number to display table :"))

#use loop to iterate
print("Multiplication Table of - ", num)
for i in range(1,11):
    print(num,'x',i,'=',num * i)

