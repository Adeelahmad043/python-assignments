# 1. Make a calculator using Python with addition , subtraction , multiplication ,
# division and power.
val1=int(input("Enter first value "))
oper=input('Enter operator')
val2=int(input("Enter second value"))
if oper == "+":
    print(val1+val2,' Answer')
elif oper =='-':
    print(val1-val2,' Answer')
elif oper =='*':
    print(val1*val2,' Answer')
elif oper =='/':
    print(val1/val2,' Answer')
elif oper =='^':
    print(val1**val2,' Answer')
else:
    print("invet text")

# 2. Write a program to check if there is any numeric value in list using for loop
clean_citie = ['Isi','Kar',"Fsd",'Qua','Phw']
val =input("Enter your city name ")
y=''
n=0
for city in clean_citie:
    if val== city:
        y=val
        print(y)
        n+=1
        break
if n == 0:
    print('no')
        



