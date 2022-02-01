#!/usr/bin/env python
# coding: utf-8

# # Python
# 
# This is readily achieved with `itables`.

# In[1]:


# example from the docs
import itables 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'cups_of_coffee': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'productivity': [2, 5, 6, 8, 9, 8, 0, 1, 0, -1]
})
df.transpose()


itables.show(df)


# In[ ]:




