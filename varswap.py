# PYTHON PORGRAM TO SWAP VARIABLES

A = input('Enter the value of A')
B = input('Enter the value of B')

#creating a temporary variable and swap the values
temp = A 
A = B
B = temp
print('The swapped value of A : {}'.format(A))
print('The swapped value of B : {}'.format(B))

