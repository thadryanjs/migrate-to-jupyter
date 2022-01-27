#!/usr/bin/env python
# coding: utf-8

# # Mixed Python and R

# In[1]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')

import pandas as pd
import numpy as np
df = pd.DataFrame({
    'cups_of_coffee': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'productivity': [2, 5, 6, 8, 9, 8, 0, 1, 0, -1]
})
df.transpose()


# In[2]:


get_ipython().run_cell_magic('R', '-i df ', 'library(ggplot2)\nggplot(df, aes(x=reorder(cups_of_coffee,productivity), y=productivity)) + geom_col() + coord_flip()')


# In[3]:


get_ipython().run_cell_magic('R', '-i df ', 'library(DT)\n# this opens it in a new tab :(\ndatatable(df)')

