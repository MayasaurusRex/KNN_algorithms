# RUN TIME ~= 2 minutes
# 
##################### PLEASE SEE ###################
# This notebook is used for getting the true ratings of the training data from the test data, to be used for analysis
# Before running this file, please run the following file to get the correct csv files needed:
    # create_true_ratings_file.ipynb --> (run time ~= 2 minutes)

# import libraries
import pandas as pd
import numpy as np
from math import sqrt

# read in the relevant data file (in this case just the first training file to reduce run time)
df1 = pd.read_csv('combined_data_1.txt', header = None, names = ['Cust_Id', 'Rating'], usecols = [0,1])

# create a new column in the dataframe to be the movie id
# this makes it easier to handle the data, but at the cost
# of time since it can take a while to clean the data
currMov = '' # track the current movie id
movie_id_row = [] # save relevant data in a new list
for row in df1.itertuples(): # iterate over the rows in the training data
    if ':' in row.Cust_Id: # if the row contains a movie id definition...
        currentMov = row.Cust_Id[:-1] # redefine the current movie id value
    movie_id_row.append(currentMov) # append the current movie to the list
    
# add the movie id coulumn to the dataframe from the list value
df1.insert(1, 'Movie_Id', movie_id_row)

# Remove the movie id definition lines to make the file easier to parse now
# that the new movie id column is created
df1 = df1[df1['Cust_Id'].str.contains(':') == False]
# change all the string values in the data frame to be float values
df1['Rating'] = df1['Rating'].astype(float)
df1['Cust_Id'] = df1['Cust_Id'].astype(int)
df1['Movie_Id'] = df1['Movie_Id'].astype(int)

# display the top 30 values of the dataframe
# for quick error checking
df1.head(30)

# read in the test data csv created earlier
answer_data = pd.read_csv('test_data.csv', header = None, names = ['Cust_Id','Movie_Id'])
# change values in the dataframe to be integers
answer_data['Cust_Id'] = answer_data['Cust_Id'].astype(int)
answer_data['Movie_Id'] = answer_data['Movie_Id'].astype(int)

# find the intersection of the two dataframes and append the rating values,
# this essentially gives us the correct ratings from the training data to 
# the probe data without having to iterate through (saves time!)
answer_data = pd.merge(df1, answer_data, on=['Cust_Id','Movie_Id'], how='inner')

# display the top 30 lines in the data frame for quick error checking
answer_data.head(30)

# save this file as a csv to avoid having to run this program every time
answer_data.to_csv('true_ratings_data.csv', index=False, header = False)