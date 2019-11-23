# 
# 1. Write a Python program to print the following string in a specific format
# (see the output).
#           Twinkle, twinkle, little star,
#                   How I wonder what you are!
#                       Up above the world so high,
#                       Like a diamond in the sky.
#           Twinkle, twinkle, little star,
#                    How I wonder what you are
# 
print("\t\tTwinkle, twinkle, little star")
print("\t\t\tHow I wonder what you are!")
print("\t\t\t\tUp above the world so high\n\t\t\t\tLike a dimond in the sky")
print("\t\tTwinkle, twinkle, little star\n\t\t\tHow I wonder what you are!")

# 2. Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)

# 3. Write a Python program to display the current date and time.
from datetime import date
today = date.today()
print("Today's date:", today)

#  4. Write a Python program which accepts the radius of a circle from the user
#  and compute the area.

rd=int(input('Enter radius = '))
ar= 3.14*rd**2
print(f"Area of the circle is = {ar}")

# 5. Write a Python program which accepts the user's first and last name an
# print them in reverse order with a space between them.

name = input("Enter your name : ")
print(f"your name in reverse order : {name[::-1]}")

# 6. Write a python program which takes two inputs from user and print them
# addition

a=int(input("Enter a number = "))
b=int(input("Enter 2nd number = "))
sun=a+b
print(f"The sum of = {sun}")

