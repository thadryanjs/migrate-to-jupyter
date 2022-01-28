#!/usr/bin/env python
# coding: utf-8

# # More Python

# Here is the second page! How great!

# ## Part two!

# In[1]:


print("Here is the other part! Huzzah!")


# In[2]:


print("hi!")


# ## Interactive tables!

# The [JupyterBooks docs](https://jupyterbook.org/interactive/interactive.html) on interactive visuals.
# 
# [jupyter-datatables](https://pypi.org/project/jupyter-datatables/) uses the JS library, but doesn't work in Lab, only standalone notebooks :(. There are open issues I could try to get involved with but it's been a few years.
# 
# A package called [itables](https://github.com/mwouts/itables)

# In[3]:


from itables import init_notebook_mode


# In[4]:


import pandas as pd
import numpy as np
df = pd.DataFrame({
    'cups_of_coffee': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'productivity': [2, 5, 6, 8, 9, 8, 0, 1, 0, -1]
})
df.transpose()


# In[5]:


import itables 
itables.show(df)


# Bingo!
