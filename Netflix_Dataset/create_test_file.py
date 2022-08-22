# RUN TIME ~= 2 minutes
# 
# This notebook takes a subsection of the probe.txt file and makes it smaller so 
# it can be used as test data points

# import libraries
import pandas as pd
import numpy as np
import math

# read in the probe.txt file that is given in the Netflix dataset
probe_data = pd.read_csv('probe.txt', header = None, names = ['Cust_Id'])

# create a new column in the dataframe to be the movie id
# this makes it easier to handle the data, but at the cost
# of time since it can take a while to clean the data
currMov = '' # track the current movie id
new_data = [] # save relevant data in a new list
for row in probe_data.itertuples(): # iterate over the rows in the probe data
    if ':' in row.Cust_Id: # if the row contains the definition of a movie id...
        currentMov = row.Cust_Id[:-1] # redefine the current movie id variable
    elif int(currentMov) <= 18: # if the movie id is less than 18 (2,135 data points in this case)
        new_data.append((row.Cust_Id, currentMov)) #add it to the new data set

# create a new dataframe with these values
test_df = pd.DataFrame(new_data, columns = ['Cust_Id', 'Movie_Id'])
test_df['Cust_Id'] = test_df['Cust_Id'].astype(int) # change string parameters to int
test_df['Movie_Id'] = test_df['Movie_Id'].astype(int) # change string parameters to int

# print out a few lines in dataframe for quick error checking...
test_df.head(30)

# save this file as a csv to avoid having to run this program every time
test_df.to_csv('test_data.csv', index=False, header = False)