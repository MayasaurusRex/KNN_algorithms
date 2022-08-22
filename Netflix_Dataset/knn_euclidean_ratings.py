# RUN TIME ~= 3 HOURS (!!!)
#
##################### PLEASE SEE ###################
# This notebook is used for applying KNN using Euclidean distance for ~24 million training points and 2,135 test points
# Before running this file, please run the following files to get the correct csv files needed:
    # create_test_file.ipynb --> (run time ~= 2 minutes)
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

# create a new dataframe based off of the training data
df_predictions = df1

# read in the test data to the knn euclidean dataframe
knn_euclidean = pd.read_csv('test_data.csv', header = None, names = ['Cust_Id','Movie_Id'])

# change the parameters from strings to integer values
knn_euclidean['Cust_Id'] = knn_euclidean['Cust_Id'].astype(int)
knn_euclidean['Movie_Id'] = knn_euclidean['Movie_Id'].astype(int)

# define the numeber of neighbors (k = 10 in this case)
num_neighbors = 10

# create a new list to store the predicted ratings for each movie
predictions = []

# iterate through the test dataframe
for row in knn_euclidean.itertuples():
    # calculate the euclidean distance between the test point and all the training points,
    # store this value as a new column (this helps to parallelize it and make more efficient)
    df_predictions['distances'] = ((row.Cust_Id-df_predictions['Cust_Id'])**2 + (row.Movie_Id-df_predictions['Movie_Id'])**2)**(1/2)
    # sort the values from lowest distance to highest distance
    df_predictions = df_predictions.sort_values(by=['distances'], ascending = True)
    # create a new list to store the neighbors
    output_values = []
    # iterate through the number of neighors defined
    for i in range(num_neighbors):
        # append the rating value of the k nearest neighbors
        output_values.append(df_predictions.iloc[i][2])
    # print the value of the vote (using the set function) 
    # --> also used as a log to ensure the program was running correctly
    # due to the long run time (3 hours)
    print(max(set(output_values), key=output_values.count))
    # save that value (the rating prediction) in the prediction list
    predictions.append(max(set(output_values), key=output_values.count))

# create a new column in the dataframe to save the rating predictions
knn_euclidean['Rating_Prediction'] = predictions
# display the top 100 lines in the dataframe for quick error checking
knn_euclidean.head(100)

# save this file as a csv to avoid having to run this program every time
knn_euclidean.to_csv('euclidean_knn_results.csv', index=False, header = False)