#!/usr/bin/env python
# coding: utf-8

# changes:
# produce different time series
# * trig
# * constant
# * online data set?

# author: Benjamin Danek
# 
# Sample Data Analysis:
# * basis/simple data analysis will be k-NN + Dynamic Time Warp
# * more advanced data analysis will be DL
# 
# Fundamentally we want to produce a program frame which can collect data from DAQ equipment, and use *some* processing on it. This means we need to allow HW feed into this program.
# 
# For now, we assume the data is stored on memory.
# 
# Classification task:
# * match recently collected data sample to a class
# * supervised setting/cluster
#     * identify which class the sample belongs to
# * unsupervised setting
#     * form classes

# In[60]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure
PLT_SIZE = 2
plt.rcParams["figure.figsize"] = (20,PLT_SIZE)


# In[54]:


# produce random signal to write t.s. analysis
sampling_length = 300 # number of samples to take -- current number is arbitrary

series_d = []

# populate series with random integers
for _ in range(sampling_length):
    signal = np.random.normal() # samples from a gaussian distribution
    series_d = np.append(series_d, signal) # series gets promoted to np.ndarray()
    
# independant series value, since it's a time series, time is the independant value
series_t = range(sampling_length)

random_signal_df = pd.DataFrame({'time' : series_t, 'signal' : series_d})
plt.plot('time', 'signal', data=random_signal_df)


# #### K-NN + DTW:

# In[55]:


# assume time series to work with is stored in random_signal_df 
# assume sample at regular intervals starting/ending at an arbitrary time
# use DTW as distance measure from samples

# methodology:
# have recently collected sample placed in a class beside its neighbors (clustering)


# In[124]:


# simulate clusters/data points: 
# series - variable with signal posed as time series (represents series, dependant value)
# center = 4, the value about which our data will be centered

def normal_series(sampling_length, center=4):
    series = [] 
    for _ in range(sampling_length):
        signal = np.random.normal(loc=center)
        series = np.append(series, np.absolute(signal))
    return series

def randint_series(sampling_length):
    low = 0; high = 7
    return np.random.randint(low, high, size=sampling_length)

def uniform_series(sampling_length):
    low = 0; high = 4
    return np.random.uniform(low, high, size=sampling_length)

def draw(series):
    plt.plot(series)
    
def draw_several(multiple_series, names=[]):
    # resize the size of the figure based off of total # of figures (else plt squishes them)
    plt.rcParams["figure.figsize"] = (20, PLT_SIZE*(len(multiple_series)))
    # draw as subplots, with shared axis
    figure, axis = plt.subplots(len(multiple_series), sharex=True)
    plt.xlabel("time, t [units]")
    for idx in range(len(axis)):
        # plot current axis
        axis[idx].plot(multiple_series[idx])
        # print name if given
        if len(names) is 0:
            axis[idx].set_title("plot: " + str(idx))
        else:
            axis[idx].set_title(names[idx])
            
# intake array of length n*m, where n is length of sample, and m is length of sample s.t. the arrays are actually n 
# separate data strings, which are sloppily combined. This method will slice the array into it's proper n parts by 
# counting indeces, and iteratively append them s.t. it returns a 2D version of the origional
# note: for future challenge, implement recursively
def multiple_append(combined, data_len):
    # exception is self explanatory, if this function is used properly, shouldn't be an issue.
    if combined % data_len is not 0:
        Except("multiple_append requires that the combined array is evenly divisible by data_len                the combined length is {} while the data_len is{}".format(len(combined), data_len))
    # number of samples
    num_data_strings = combined/data_len
    mult_d_arr = [[]]
    for component in range(num_data_strings):
        current_arr = combined[(component*data_len):((component+1)*data_len)]
        mult_d_arr = np.append(mul_d_arr, current_arr, axis=0)
    #to-do {complete}


# In[76]:


num_samples = 500

norm = normal_series(num_samples) 
rand = randint_series(num_samples)
uniform = uniform_series(num_samples)

draw_several([norm, rand, uniform], ["norm", "rand", "uniform"])


# In[122]:


# in order to perform our proof of concept, we need to either collect data, or simulate it's existance. This function
# does the latter, by producing a set amount of data points of each class, where a class of data is defined as an 
# identity to the source of data.
# we will make n of each class, and add it to one data set, which will be the basis for our data processing practice
def simulate_data(data_set_size, num_samples):
    data_set = []
    print(data_set)
    for _ in range(data_set_size):
        norm = normal_series(num_samples) 
        rand = randint_series(num_samples)
        uniform = uniform_series(num_samples)
        
        # requires a fix w/ thorough ray appending
        temp = np.append(np.append(norm, rand), uniform)
        
        data_set = np.append(data_set, [[norm], [rand], [uniform]], axis=0)
    return data_set


# In[123]:


(simulate_data(3, 10))


# In[127]:


for id in range(10):
    print(id)


# In[ ]:




