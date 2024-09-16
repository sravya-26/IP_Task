#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

all_walks = []

# Simulate 500 random walks
for i in range(500):  
    random_walk = [0]  
    for x in range(500):  # Each walk has 500 steps
        step = random_walk[-1]  
        dice = np.random.randint(1, 7) 
        
        # Determine the next step based on dice roll
        if dice <= 2:
            step = max(0, step - 1)  # Decrease the step (but not below 0)
        elif dice <= 5:
            step += 1  
        else:
            step += np.random.randint(1, 7)  # Big jump if dice rolls 6
        
        # 0.1% chance of falling to step 0
        if np.random.rand() <= 0.001:
            step = 0
        
        random_walk.append(step) 
    
    all_walks.append(random_walk)  

np_aw_t = np.transpose(np.array(all_walks))

ends = np_aw_t[-1, :] 

plt.hist(ends, bins=50) 
plt.title('Distribution of Random Walk Endpoints')
plt.xlabel('Final position')
plt.ylabel('Frequency')
plt.show()

