# Given three numbers find the maximum of three numbers using the ternary operator.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max_number = a if(a>b and a>c) else (b if b>c else c)
print ("the maximum number is: ", max_number)
