
# coding: utf-8

# In[1]:


import os
import pypianoroll as pn


# In[3]:


os.chdir('./archive/new_songs/')


# In[8]:


subdir = [dI for dI in os.listdir('.') if os.path.isdir(os.path.join('.',dI))]
ko = 0
po = 0
for i in subdir:
    po += 1
    os.chdir(i)
    a = pn.parse('all.mid')
    b = pn.parse('melody.mid')
    if(a.get_active_length() >= b.get_active_length()):
        ko+=1
    os.chdir("..")

print ko*100.0/po

