Q1. WAP to input 2 strings and swap the strings 

Sol1.

	def swap_no(x, y):
		x , y = y , x
		print('After swapping', x, y)
	x, y = input('Enter the two numbers ').split(' ')
	swap_no(x,y)
	
---------------------------------------------

Q2.  WAP to generate 4 random numbers in the range 0-26 and print their average 

Sol2. 
	from random import randint
	def random_no():
		i = 0 
		total = 0
		while(i < 4):
			total += randint(0, 26)
			i += 1
		print(total/4)
	random_no()
	
-----------------------------------------------------------------

Q3. WAP to generate and print a random uppercase or lowercase alphabet. Try these: 

 i) Create a string containing all alphabets and then select a random alphabet. 
 
 Sol. 
	from string import ascii_letters as al
	from random import randrange

	print(al[randrange(len(al))])
	
	
 ii) Check the module string 
 
 Sol.
	import string
	dir(string)
	
----------------------------------------------------------------------------

Q4. WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple Interest

Sol4.

	def get_si(p, r, t):
		si = (p * r * t)/100
		print("Simple interest is %d " % (si))
	p, r, t = [float(x) for x in input("Enter p, r and t ").split(' ')]
	get_si(p, r, t)
	
--------------------------------------------------------------------------

Q5.  WAF get_amount() that takes Principle, Rate and Time as arguments and returns the Total amount using the get_si() 
function from above to calculate the SI. 
Also provide Rate = 10 and Time = 1 as default arguments. 

Sol5.

	def get_si(p, r= 10, t = 1):
		return(p * r * t)/100

	def get_amount(p, r= 10, t = 1):
		amount = p + get_si(p, r, t)
		print("amount is %d" % (int(amount)))
	# p, r, t = [float(x) for x in input("Enter p, r and t ").split(' ')]
	get_amount(100 , 1, 4)
	
------------------------------------------------------------------------------

Q6.  WAP get_ci() that takes Principle, Rate and Time as arguments and returns the Compound Interest. 

Sol6.
	def get_ci(p , r, n , t):
		ci = p * (pow( 1 + (r/(100 * n)), n * t))
		print("Compound interest is %d" % ci)
	p, r, n , t= [float(x) for x in input("Enter p, r ,n  and t ").split(' ')]
	get_ci(p , r, n, t)
	
-------------------------------------------------------------------------

Q7. WAP get_q_r() taking 2 numbers as parameters and returns the quotient and remainder in the form of a tuple. 

Sol7.

	def get_q_r(x , y):
		s = (x/y , x%y)
		print("Quotient and remainder is {}".format(s))
	x , y  = map(float, input("Enter two no's").split())
	get_q_r(x, y)
	
----------------------------------------------------------------------------

Q8. WAP to find the length of hypotenuse of a right angled triangle, input the height and base from user

Sol8.

	from math import sqrt
	def hyp_len(h, b):
		parameters = [h**2 , b**2]
		hyp_length = sqrt(sum(parameters))
		print('The length of hypotenuse is %f' % hyp_length)
	h, b = map(float, input("Enter length and base of a triangle ").split(' '))
	hyp_len(h, b)
	
---------------------------------------------------------------------------------------

Q9. WAP to input number of seconds and print in days, hours, minutes and seconds 

Sol9. 

	def convert(s):
		d = s / 86400
		s = s % 86400
		h = s / 3600
		s = s % 3600
		m = s / 60
		sec = s % 60
		print(" %d %d %d %d " % (d , h, m , sec))
	s = float(input("Enter seconds"))
	convert(s)
	
-------------------------------------------------------------------------------

Q10. Check your version of python interpreter without opening the interpreter 
(Which command needs to be used on the command line). 

Sol10. 

	import sys
	sys.version
	
----------------------------------------------------------------------------

Q11. Find output

Sol11. 

	2, -2
	
----------------------------------------------------------------------------

Q12. Find output

Sol12.

	None
	
------------------------------------------------------------------------

Q13.  WAP to input the real and imaginary part of a complex number and
 print it on screen. output should look like   re:10 im:20 

Sol13.

	def complex_cal(x , y):
		z= complex(x , y)
		print("re: %d im: %d" % (z.real, z.imag))
	x, y = map(float, input("Enter real and imaginary input ").split())
	complex_cal(x, y) 
	
-----------------------------------------------------------------
    