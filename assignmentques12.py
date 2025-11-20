# ques12 assignment
import math
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

g = math.gcd(a, b)
l = (a * b) // g

print("HCF of", a, "and", b, "is", g)
print("LCM of", a, "and", b, "is", l)
