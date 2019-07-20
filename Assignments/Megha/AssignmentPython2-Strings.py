
Q1. Guess output of each slice:   
	s=‘Python is Object Oriented’ 
	
Sol1. s[-1] =d
	  s[::-1] = detneirO tcejbO si nohtyP
	  s[:-1] = Python is Object Oriente
	  s[1:1] = Prints nothing
	  s[4:10] = on is
	  
--------------------------------------------------------------

Q2. What error do you see for following statements:  
s= ''
print(s[1]) 

Sol2.

IndexError                                Traceback (most recent call last)
<ipython-input-2-c803f0c3658b> in <module>
      1 s = ''
----> 2 print(s[1])

IndexError: string index out of range


----------------------------------------------------------------

Q3. Do you get any error for the following code, if not give the output:  
	S=‘Gaurav’  
	print(s[1]) 


Sol3. a

------------------------------------------------------------------------


Q4. Find the o/p

a.	s='a b cd'
	print(len(s)) 
	print(s[::2]) 
	print(len(s[::2]))
	
Sol. 6
	abc
	3
-------------------------------------------	

b.	s='a#b#c#d#' 
	print(s.split()) 
	print(s.split('#')) 
	l=s.split('#')
	s='$'.join(l)
	print(s)

Sol. ['a#b#c#d#']
	['a', 'b', 'c', 'd', '']
	 a$b$c$d$
--------------------------------------------------	

c.	 S=‘Gaurav’ 
	 S=S[::-2][::-2] 
	 print(S) 
	 
Sol.  av

-------------------------------------------------

d.	print(1>2)
	
Sol. False

-------------------------------------------------

e.	print(4%2, 5%2, 2%5, sep=',') 
	
Sol. 0,1,2

------------------------------------------------

f.	s='abcba'
	s.upper() 
	print(s) 
	print(s.count('A'), end = ',') 
	print(s.count('A', 2,4) , end = ',')  
	print(s.count('a', 2,4) , end = ',') 
	
	
Sol. abcba
	 0,0,0
	 
------------------------------------------------

Q5.  WAP to input a string and remove all spaces from it. 

Sol5. 
	s = input('Enter a string');
	l = s.split()
	p =''.join(l)
	print(p)
	
-----------------------------------------------------------

Q6. What does this symbol denote: [] 

Sol6. An object of a list.

--------------------------------------------------------------

Q7. WAP to print all methods(functions/operations) available in a string (Hint : dir()) 

Sol7.

	def find_all_methods(arg):
		print(dir(arg))
	find_all_methods('str')
	
-------------------------------------------------------------

Q8. Write statement to check if rstrip method is available in the str class. (Hint : Use the find function or in) 


Sol8. 

	'rstrip' in dir(str)
	
-------------------------------------------------------------------


Q9. WAP to store the following patterns in a string variable and then print them


Sol9. 
	s = '''                
	*****      *     *          ________
	  *        * * * *         |        |
	  *        *  *  *         o        |
	  *        *     *        /|\       |
	  *                       / \       |
										|
							____________|
					
					
		'''
		
	print(s) 
	
-----------------------------------------------------------------------

Q10.  WAP to input a string and replace all space with new lines (\n) and print again. 

Sol10.

	s = input()
	print(s.replace(' ', '\n'))
	
--------------------------------------------------------------------------


Q11. WAP to input complete name(first and last name separated by space) and print first and last name separately along with their length in upper case.

Sol11.

	f_name,l_name = input('enter first name & last name').split(' ')
	print(f_name.upper() , len(f_name))
	print(l_name.upper() , len(l_name))
	
----------------------------------------------------------------------------

Q12. WAP to input a string and split it into 2 halves. The string can be of any length 


Sol12.

	s = input()
	m = len(s)
	n = int(m/2)
	print(s[:n:1])
	print(s[n::1])
	
--------------------------------------------------------------------------------




