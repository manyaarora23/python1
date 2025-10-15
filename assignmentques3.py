# John is trying to solve the arithmetic series(AP). He wants to find two things in the series
#1. He wants to find nth terms in the series
#2. He wants to find the sum up to the nth term.

a = float(input("Enter the first term: "))
d = float(input("Enter the comman difference: "))
n = float(input("Enter the number of terms: "))
nth_term = (a+(n-1)*d)
print("The nth term is : ",nth_term)
sum = (n/2)*(2*a + (n-1)/d)
print("The sum of the terms is : ", sum)
