#!/usr/bin/env python
# coding: utf-8

# In[5]:


# prob 1
def max_func(*args):
    if args == ():
        return "No numbers given."
    res = args[0]
    for arg in args:
        if arg > res:
            res = arg
    return res

max_func()


# In[6]:


# prob 2
def decorator2(f):
    def wrapper():
        str = f()
        print('<u>', str, '</u>')
    return wrapper

def decorator(f):
    def wrapper():
        return f() + ", it's me!"
    return wrapper

@decorator2
@decorator
def dummy():
    return "Hi"

dummy()


# In[7]:


# prob 3
def my_range(n):
    for i in range(n):
        yield(i)
    yield "There are no values left."
    
num = my_range(3)
for i in range(20):
    print(next(num))


# In[12]:


# prob 4
import Customer


# In[15]:


run Customer

