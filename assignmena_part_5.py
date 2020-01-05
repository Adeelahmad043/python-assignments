'''                   Python Assignment # 5
Question:1
Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to the factiorial : "))
print(factorial(n))
'''
Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters.'''

def s_t(s):
    d={"upper_case":0, "lower_case":0}
    for i in s:
        if i.isupper():
           d["upper_case"]+=1
        elif i.islower():
           d["lower_case"]+=1
        else:
           pass
    print (f"Original String : {s} ")
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

s_t('The quick Fox')
'''
Question:3
Write a Python function to print the even numbers from a given list.
'''
list1 = [10, 21, 4, 45,22,34,54,55,66, 93]  
even_nos = [num for num in list1 if num % 2 == 0] 
  
print(f"Even numbers in the list: {even_nos}")
        
'''
Question:4
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
backward as forward, e.g., madam'''

def Pali(st):
	le_pos = 0
	ri_pos = len(st) - 1
	
	while ri_pos >= le_pos:
		if not st[le_pos] == st[ri_pos]:
			return False
		le_pos += 1
		ri_pos -= 1
	return True
print(Pali('696'))

'''
Question:5
Write a Python function that takes a number as a parameter and check the
number is prime or not.'''

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 
pr= int(input('Enter a prime number'))            
print(test_prime(pr))