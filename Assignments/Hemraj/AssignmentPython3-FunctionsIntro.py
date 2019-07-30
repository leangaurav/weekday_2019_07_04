#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = input("Enter a first string:")
b = input("Enter a second string:")
temp = a
a = b
b = temp
print(a, b)


# In[31]:


from random import randint
sum=0
for i in range(4):
    print(randint(0,26))
    sum = sum + randint(0,26)
print(sum)
print("average of random numbers:", sum/4)
    


# In[43]:


p = int(input("enter the principle:"))
r = int(input("enter the rate:"))
t= int(input("enter the time:"))
def get_si(p,r,t):
    si = (p*r*t)/100
    print(si)
get_si(p,r,t)


# In[47]:


def get_si(p,r,t):
    si = (p*r*t)/100
    print(si)
get_si(1000,10,5)

def get_amount(p, r, t):
    si =(p*r*t)/100
    amount = si + p
    print(amount)
get_amount(1000, 10, 1)
    


# In[51]:


def get_ci(p,r,n,t):
    ci = p * (pow((1 + r / 100), n*t))
    print(ci)
get_ci(1000,10,5,2)


# In[62]:


def get_q_r(a,b):
    q = a/b
    print(q)
    r = a%b
    print(r)
    return q,r
q,r=get_q_r(100,6)
l = []
l.append(q)
l.append(r)
t = tuple(l)
print(t)


# In[68]:


import math
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
h = math.sqrt(a**2 +b**2)
print(h)


# In[80]:


sec=int(input('Enter seconds'))
day = int(sec/86400)
sec = sec%86400
hour= int(sec/3600)
sec= sec%3600
min= int(sec/60)
sec = int(sec%60)


print(day,hour,min,sec)


# In[83]:


import sys
sys.version


# In[86]:


x = 2
x*=3
x = x%4
y = -x
print(x, y)


# In[87]:


def func():
    pass

print(func())


# In[92]:




re = int(input("Enter the real part of complex number:"))
im = int(input("Enter the imaginary part of complex number:"))
c = complex(re, im)
print('re:',c.real,' im:', c.imag)


# In[95]:


def input_complex(r, i):
    t = (r,i)
    return t
r = int(input("enter the real number"))
i = int( input("enter the imag number"))
input_complex(r,i)


# In[98]:


def print_complex(re,im):
    return re,im

real= input('Enter real part of complex number')
imag= input('Enter imag part of complex number')
print_complex(real,imag)


# In[99]:


def add(re1,im1,re2,im2):
    re=re1+re2
    im=im1+im2
    return re,im
def sub(re1,im1,re2,im2):
    re=re1-re2
    im=im1-im2
    return re,im

print(add(10,20,5,-30))
print(sub(10,20,5,-30))


# In[100]:


def div(re1,im1,re2,im2):
    re=re1/re2
    im=im1/im2
    return re,im
def mul(re1,im1,re2,im2):
    re=re1*re2
    im=im1*im2
    return re,im
def conj(re1,im1):
    conj=re1-im1
    return conj

print(div(10,20,5,-30))
print(mul(10,20,5,-30))
print(conj(10,20))

