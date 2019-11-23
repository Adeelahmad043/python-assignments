#                              Assignment # 2
# 1. Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?
print("Enter your marks of weekend test")
a=int(input("math     :"))
b=int(input('English  :'))
c=int(input("Urdu     :"))
d=int(input("Computer :"))
e=int(input("Science  :"))
total=a+b+c+d+e
avg= total/500*100
if avg>90:
    print(f"marks ={total}/500 Grades A+ ")
elif avg>80:
     print(f"marks ={total}/500 Grades A")
elif avg>70:
     print(f"marks ={total}/500 Grades B")
elif avg>60:
     print(f"marks ={total}/500 Grades C")
elif avg>50:
     print(f"marks ={total}/500 Grades D")
else:
     print(f"marks ={total}/500 Fail")

# 2. Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)
#                             Assignment # 2
# 3. Write a program which take input from user and identify that the given
# number is even or odd?
​
num=int(input("Enter a number to find Even or not"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write a program which print the length of the list?
arr = [1,2,3,4,5,6,7,8,9]
print(len(arr))

# 4. Write a Python program to sum all the numeric items in a list?
num = [9,8,7,6,5,4,3,2,1]
i=0
total=0
while i < len(num):
    total = total + int(num[i])
    i += 1
print (total)

# 5. Write a Python program to get the largest number from a numeric list.
num = [91,28,7,6,15,44,39,99,1]
i=0
total=0
for i in num:
    if total<i:
        total=i   
print (total)

# 6. Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are
# less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less=0
for i in a:
    if i<5:
        less=i
        print(less)
