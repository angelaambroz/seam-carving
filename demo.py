
# coding: utf-8

# In[5]:


import os
from seam_carving import SeamCarver


# In[6]:


# !pip install opencv-python


# In[8]:


ls


# In[9]:


folder_in = 'in'
folder_out = 'out'
filename_input = 'test.png'
filename_output = 'test_result.jpg'
filename_mask = 'mask.png'


# In[11]:


input_img = os.path.join(folder_in, filename_input)
input_mask = os.path.join(folder_in, filename_mask)
output_img = os.path.join(folder_out, filename_output)


# In[20]:


obj = SeamCarver('in/test.png', 0, 0, object_mask='in/mask.png')
obj


# In[ ]:




