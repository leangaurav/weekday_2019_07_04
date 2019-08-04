
Q1. WAP to print first n natural numbers (input n from user)

Sol1.
    
x = int(input("Enter n "))
print("First %d natural nos are:" % x)
for i in range(1, x+1):
    print(i, end = " ")
    
-------------------------------------------------------------------------

Q2.  WAP to find sum of first n natural numbers 

Sol2.

x = int(input("Enter n "))
sum = 0
print("Sum of First %d natural nos are:" % x)
for i in range(1, x+1):
    sum += i
print(sum)

-----------------------------------------------------------------------

Q3. WAP to print first n natural numbers in reverse order

Sol3. 

x = int(input("Enter n "))
sum = 0
print(" First %d natural nos in reverse order:" % x)
for i in range(x , 0 , -1):
    print(i , end = " ")
    
--------------------------------------------------------------------------


Q4. WAP to input a number and print its factorial. 

Sol4.

x = int(input("Enter n: "))
fact = 1

for i in range(1, x+ 1):
    fact *= i
print("Factorial of %d is: %d" % (x , fact))

-----------------------------------------------------

Q5. WAP to print Fibonacci sequence till n. 

Sol5. 

x = int(input("Enter n: "))
a = 0
b = 1
i = 1
c = 0
print("The fibonnaci series till %d is :" % (x))
while c <= x :
    print(c, end = " ")
    temp = b
    b = c
    a = temp
    c = a + b
    
----------------------------------------------------


Q6. WAP to print all digits of a number input from user. 

Sol6. 

x = int(input('enter the no: '))
print("All the digits of a no entered are: ")
while(x > 0):
    r = x % 10
    x = int(x / 10)
    print(r)
    
 ---------------------------------------------------------------
 
 
 Q7. WAP to find sum of all digits of a number
 
 Sol7.
 
 m = int(input('enter the no: '))
sum = 0
x = m
while(x > 0):
    r = x % 10
    x = int(x / 10)
    sum += r
print("The sum of the digits of %d is: %d" % (m, sum))

-------------------------------------------------------------------

Q8. WAP to find sum of following series given n as input from user 
1 + 2! + 3! + 4! + 5! + ….n! Where n! denotes the factorial of number n. 

Sol8.

def factorial_no(x):
    fact = 1
    for i in range(1, x+ 1):
        fact *= i
    return fact
n = int(input("Enter no: "))
j = n
summ = 0
while n >= 1:
    summ += factorial_no(n)
    n-= 1
print("The sum of factorial series of %d is %d" % (j, summ))

----------------------------------------------------------------------

Q9. WAP to input base and exponent and print result without using inbuilt function pow(use for or while loop). 

Sol9.

def pow_cal(x, y):
    power = 1
    for i in range(1, y+1):
        power*= x
    print("the output is %d" % power)
x , y = map(int, (input("Enter x and y ")).split(' '))
pow_cal(x, y)

-----------------------------------------------------------------

Q10. Print Pattern

Soli)

for i in range(1, 6):
    for j in range(i):
        print("*", end = " ")
    print()
  
----------------------------------------

Solii)

for i in range(5, 0 , -1):
    for j in range(i):
        print("*", end = " ")
    print()
    
------------------------------------------

Soliii)

for i in range(5, 0 , -1):
    next = i;
    while i > 1:
        print(" ", end = " ")
        i-= 1
    for m in range(next , 6):
        print("*", end = " ")
    print()
    
 ----------------------------------------------
 
 Soliv)
 
 for i in range(5, 0 , -1):
    next = i;
    while i > 1:
        print(" ", end = "")
        i-= 1
    for m in range(next , 6):
        print("*", end = " ")
    print()
    
  ---------------------------------------
  
  
  Q11. Print Pattern
  
  Soli.
  
  for i in range(1, 6):
    for k in range(i):
        print(i, end = " ")
    print()
    
    
  ----------------------------------------------
  
  
  Solii) 
  
  for i in range(1, 6):
    for k in range(1, i+1):
        print(k, end = " ")
    print()
    
  -----------------------------------
  
  Soliii)
  
  for i in range(5, 0 , -1):
    for k in range(i , 6):
        print(i, end = " ")
    print()
    
    
  ---------------------------------
  
  Soliv) 
  
    for i in range(1, 6):
        space = 6
        while(space >= i):
            print(" ", end = " ")
            space -= 1
        for k in range(i):
            print(i, end = " ")
        print()
        
  -----------------------------------
  
  
  Q12 . Print Pattern
  
  
  Soli)
  
  for i in range(1, 6):
    for k in range(1, i+1):
        print(chr(64+ k) , end = " ")
    print()
    
    
 ----------------------------------
 
 Solii)
 
 s = 1
for i in range(1, 6):
    for k in range(1, i+1):
        print(chr(64 + s) , end = " ")
        s += 1
    print()
    
 
 -------------------------------------------
 
 
 Soliii) 
 
 for i in range(1, 6):
    for k in range(1, i+1):
        print(chr(64+ i) , end = " ")
    print()
    
    
------------------------------------------


Soliv)


 for i in range(1, 6):
        m = 6
        while i <= m:
            print(" " , end = " ")
            m-= 1
        for k in range(1, i+1):
            print(chr(64+ k) , end = " ")
        next = k - 1
        while next >= 1:
            print(chr(64 + next), end = " ")
            next -= 1
        print()
        
        
 ---------------------------------------------------
    
    
------------------------------------------------


Soliv)


  






