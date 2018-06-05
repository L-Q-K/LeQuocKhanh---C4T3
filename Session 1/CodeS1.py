import os
import time

#2.Write a program that calculates the area of a circle. The circle radius is entered by users:
r = float(input('Radius: '))
a = r**2 * 3.14
print("The area of the circle with radius =", r, "is", a)
input("Enter for the next exercies")
os.system('cls')

#3.Write a program that converts Celsius (0C) into Fahrenheit (0F) .Expected screen output:
c=float(input('In Celcius: '))
f = c*1.8 +32
print(c," in Celcius =", f, 'in Fahrenheit')
time.sleep(3)

