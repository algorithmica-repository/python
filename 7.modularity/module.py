#!/usr/bin/env python
# coding: utf-8

# In[1]:


#module: A group of related functions, classes and datasets


# In[7]:


def add(a, b):
    return a+b+1


# In[3]:


def sub(a, b):
    return a-b


# In[5]:


def mul(a, b):
    return a*b


# In[9]:


#print(__name__)
if __name__ == "__main__":
    assert add(10, 20) == 30
    assert sub(10, 20) == -10
    assert mul(10, 20) == 200


# In[ ]:




