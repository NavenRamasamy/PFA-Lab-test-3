#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install httpimport


# In[1]:


import httpimport
url = "https://raw.githubusercontent.com/deep-bits/PFA/main/Python-tutorials/"
with httpimport.remote_repo(url):
    import circle as c
    import Factorial_via_iteration as f
print("Area of a circle with radius =",4,"is",c.area(4))


# In[2]:


print("Factorial of",4, "is",f.factI(4))


# In[ ]:




