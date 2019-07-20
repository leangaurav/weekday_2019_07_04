Q1. Input temperature in Fahrenheit in print in Celsius

Sol1.

def temp(f):
    c = (f - 32) * 5 / 9
    print(c)
f = float(input("Enter temp in fahrenheit"))
temp(f)

--------------------------------------------------------------


Q2. Write a program to input a number and print its square and cube. 

Sol2.

def oper(x):
    sqr = x * x
    cub = x * x * x
    print(sqr)
    print(cub)
x = float(input("Enter a number"))
oper(x)

-------------------------------------------------------------------

Q3. WAP to input a number n and a number m and print the result of following 
n2 + m2 

Sol3. 

from numpy import square
def func(n , m):
    s = square(n) + square(m)
    print(s)
n , m = map(float , input("Enter both no's\t").split())
func(n, m)

--------------------------------------------------------------------------------


Q4.   WAP to input a numbers M and N and print result of MN. (use both ** and pow) 

Sol4.

def func(m , n):
    x= pow(m,n)
    y = m ** n
    print(x)
    print(y)
m , n = map(float , input("Enter both no's\t").split())
func(m ,n)

--------------------------------------------------------------------------------------


Q5. Write a simple interest calculator. 

Sol5.

def si(p , r, t):
    amount = p * (1 + (r * t))
    print(amount)
p, r, t =[float(x) for x in input('Enter p, r, t\t').split()]
si(p, r, t)


---------------------------------------------------------------------------------


Q6. Input Principal, Rate, Time and print Compound Interest and Amount. 


Sol6.

def ci(p , r, t):
    amount = p * pow(1+r/100, t)
    ci = amount - p
    print(amount)
    print("ci is" , ci)
p , r, t = [float(x) for x in input("Enter p, r and t\t").split()]
ci(p , r, t)


---------------------------------------------------------------------


Q7. WAP to print sum of first n natural numbers. (n needs to be taken as input). 


Sol7.

def sumofno(n):
    print(int((n * (n + 1))/2))
n = int(input("Enter the no"))
sumofno(n)

-----------------------------------------------------------------------------


Q8.  WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and also the pythonic way)

Sol8.

def swap(x , y):
    a1 , a2 = y , x
    temp = y
    y = x
    x = temp
    print("Output using python ", a1 , a2)
    print("Output using temp" , x , y)
x , y  =map(int, input("Enter both no").split()) 
swap(x, y)  

----------------------------------------------------------------------------------------

Q9.  WAP to print ascii value of all white-space characters present in python. 

Sol9. 

def calc():
    white_space_char = ['\t' , '\n' , '\r', '\v', '\f', ' ']
    i = 0
    while i < len(white_space_char):
        print(ord(white_space_char[i]))
        i+=1
calc()    

-------------------------------------------------------------------------------------


Q10. Input a single character and print its ascii values.


Sol10.

def ascii_cal(x):
    if len(x) == 1 and x.isalpha() == True:
        print(ord(x))
    else:
        print("Re-enter the correct input char")
x = input("Enter a single char ")        
ascii_cal(x)

----------------------------------------------------------------------------------


Q11. WAP that takes area of a circle and gives back the radius and circumference. 

Sol11.

from math import pi , sqrt

def func(a):
    print('Radius and circumference is ' ,sqrt(a / pi) , 2 * pi * sqrt(a / pi))
a = float(input("Enter the area"))
func(a)
    
-----------------------------------------------------------------------------


Q12.  We need to input marks in 5 subjects out of 100 and print percentage


Sol12.

def cal(numbers):
    print(sum(numbers)/ 500 * 100)
    
while True:
    try:    
        a , b ,c , d, e = [float(x) for x in input("Enter marks of 5 subjects out of 100 ").split()]
        numbers = [a , b, c, d, e]
        cal(numbers)
    except ValueError:
        print("Try again, Enter valid input") 
	break

------------------------------------------------------------------------------------------		

