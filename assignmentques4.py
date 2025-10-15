#Write a program that converts and prints user given measurement in inches into
#1. foot(12 inches)
#2. yard(36 inches)
#3. centimetres(2.54 inches)
#4. meter(39.37 inches)

inches = float(input("Enter the measurements in inches : "))

foot = inches/12
yard = inches/36
centimeter = inches*2.54
meter = inches/39.37

print("Convertes measurements are:")
print("Feets : ",foot)
print("Yards : ",yard)
print("Centimeter : ",centimeter)
print("Meter : ",meter)
