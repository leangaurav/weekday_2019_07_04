Q1.  Convert a Tuple t = (1,2,3,4,5) to a list 

Sol1. 

	t = (1,2,3,4)
	l = list(t)
	print(l)
	
-------------------------------------------------------

Q2. WAP to join a list and a tuple:  L = [1,3,5,7]   T = (8,6,4,2) 
	Store the result in a list LS 
	
Sol2. 

	L = [1,3,5,7]
	T= (8,6,4,2)
	LT = L + list(T)
	print(LT)
	
----------------------------------------------------------

Q3.  What is difference between list and tuple. 

Sol3.
	List        |        Tuple
	
-  mutable				immutable

--------------------------------------------------------------

Q4.  Print the list in reverse order  l = [‘a’, ‘d’, ‘c’, ‘A’, ‘C’] 

Sol4.  

	l = ['a', 'd' , 'c', 'A', 'C']
	print(l[::-1])  

--------------------------------------------------------------

Q5.  Print Elements at Odd indexes from a list (Do not use loop)   
	l = [10,11,20, 21,30, 31, 40, 41]  

Sol5. 	

	l = [10,11,20, 21,30, 31, 40, 41]  
	print(l[::2])
	
----------------------------------------------------------------

Q6. How many ways you can copy a list. 

Sol2. 1. list.copy()
      2. Slicing (l:)
	  
---------------------------------------------------------------


Q7. Predict Output

Sol7. 

	a
	5
	
-----------------------------------------------------------------------


Q8. Predict Output

Sol8.

	[1, 4, 6, 8]
	[1, 3, 5, 7]
	
-------------------------------------------------------------


Q9. Predict Output

Sol9.

	[1 , 3, 5, [7, 9]]
	[1 , 3, 5, [7, 9], 11, 13]
	
-------------------------------------------------------------

Q10. Predict Output

Sol10.

	 <class 'tuple'>
     <class 'int'>
     <class 'int'>
     <class 'tuple'>
	 
----------------------------------------------------------

Q11. Print matrix

Sol11.

	a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	for row in a:
		for elem in row:
			print(elem , end = ' ')
		print('')
		
-------------------------------------------------

Q12. Predict Output

Sol12. t2 is not defined

-----------------------------------------------

Q13. Predict Output

Sol13.

	('s', 't', 'r', 'i', 'n', 'g')
	('g', 'n', 'i', 'r', 't', 's')
	('n', 's')
	
---------------------------------------------

Q14. Predict Output

Sol14.

	True
	False
	1
	0
	
-----------------------------------------------

Q15. Write a program to input a string and print if it is palindrome or not. 

Sol15

	t = input()
	r = int(t in t[::-1])
	pal = ['not a palindrome','palindrome']
	print('The input string %s is %s' % (t, pal[r]))
	
-------------------------------------------------------------

Q16.  Use the range method and create a tuple containing the following values: (20, 15, 10, 5) 

Sol16.

	s = range(5, 25 , 5)
	t = list()
	for x in s:
		t.append(x)
	t = t[::-1]
	print(tuple(t))
	
-------------------------------------------------------------

Q17. WAP to convert string to list of characters. 

Sol17.

	x = input()
	print(list(x))
	
-----------------------------------------------------------------

Q18. Predict Output

Sol18.

	<class 'list'>
	<class 'NoneType'>
	<class 'str'>
	<class 'bool'>
 
--------------------------------------------------------------------------------

Q13. 