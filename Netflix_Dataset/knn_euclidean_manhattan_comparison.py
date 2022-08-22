# RUN TIME ~= 1 minute
# 
##################### PLEASE SEE ###################
# This notebook is used for the testing and comparison of the Euclidean and Manhattan implementations of KNN
# Before running this file, please run the following files to get the correct csv files needed:
    # create_test_file.ipynb --> (run time ~= 2 minutes)
    # create_true_ratings_file.ipynb --> (run time ~= 2 minutes)
    # knn_euclidean_ratings.ipynb --> (run time ~= 3 hours)
    # knn_manhattan_ratings.ipynb --> (run time ~= 3 hours)

# import libraries
import pandas as pd
import numpy as np
from math import sqrt
from plotly import graph_objects as go

# load in the data to be used for analyzing test results between the euclidean and manhattan implementations:
    # correct values from the test data file, created by create_true_ratings.ipynb file
correct_ratings = pd.read_csv('true_ratings_data.csv', header = None, names = ['Cust_Id', 'Movie_Id', 'Rating'])
    # predicted ratings for the test data file using euclidean knn implementaion, created by knn_euclidean_ratings.ipynb file
euclidean_ratings = pd.read_csv('euclidean_knn_results.csv', header = None, names = ['Cust_Id', 'Movie_Id', 'Rating'])
    # predicted ratings for the test data file using manhattan knn implementaion, created by knn_manhattan_ratings.ipynb file
manhattan_ratings = pd.read_csv('manhattan_knn_results.csv', header = None, names = ['Cust_Id', 'Movie_Id', 'Rating'])

# calculate the RMSE value for the euclidean implementation of KNN
# this takes into account how close the values were, not just right vs. wrong
euclidean_rmse = ((correct_ratings.Rating - euclidean_ratings.Rating) ** 2).mean() ** .5
print("The Euclidean KNN implementation had a RMSE of: " + str(euclidean_rmse))

# calculate the RMSE value for the manhattan implementation of KNN
# this takes into account how close the values were, not just right vs. wrong
manhattan_rsme = ((correct_ratings.Rating - manhattan_ratings.Rating) ** 2).mean() ** .5
print("The Mahattan KNN implementation had a RMSE of: " + str(manhattan_rsme))

# calculate the accuracy of the euclidean KNN implementation
euclidean_accuracy = list() # track accuracy, save as a vector to track how it acts over time
sum_correct = 0 # track the values that were correctly predicted

# iterate through the euclidean ratings
for i in range(len(euclidean_ratings)):
    # compare the predictions with the correct ratings
    if (euclidean_ratings.iloc[i][2] == correct_ratings.iloc[i][2]): # if the prediction was accurate...
        sum_correct = sum_correct + 1 # increment the total correct sum value
    euclidean_accuracy.append((sum_correct/(i+1)) * 100) # update the accuracy

# Display overall accuracy at the end of 2,135 points...
print("The Euclidean KNN implementation had " + str(sum_correct) + " correct ratings")
euclidean_ratings['Correct_Count'] = euclidean_accuracy # add the vector as a column to the euclidean dataframe
euclidean_ratings.head(30) # display top of the file for quick error checking

# calculate the accuracy of the manhattan KNN implementation
manhattan_accuracy = list()# track accuracy, save as a vector to track how it acts over time
sum_correct = 0 # track the values that were correctly predicted

# iterate through the manhattan ratings
for i in range(len(manhattan_ratings)):
    # compare the predictions with the correct ratings
    if (manhattan_ratings.iloc[i][2] == correct_ratings.iloc[i][2]): # if the prediction was accurate...
        sum_correct = sum_correct + 1 # increment the total correct sum value
    manhattan_accuracy.append(sum_correct/(i+1)*100) # update the accuracy

# Display overall accuracy at the end of 2,135 points...
print("The Manhattan KNN implementation had " + str(sum_correct) + " correct ratings")
manhattan_ratings['Correct_Count'] = manhattan_accuracy # add the vector as a column to the manhattan dataframe
manhattan_ratings.head(30) # display top of the file for quick error checking

# plot the overall accuracy, tracking as more test data points run
fig = go.Figure() # create a new figure object
# add the euclidean accuracy trace
fig.add_trace(go.Scatter(x=euclidean_ratings.index, y=euclidean_ratings.Correct_Count, mode='lines', name='Euclidean Accuracy'))
# add the manhattan accuracy trace
fig.add_trace(go.Scatter(x=manhattan_ratings.index, y=manhattan_ratings.Correct_Count, mode='lines', name='Manhattan Accuracy'))
# add title and labels
fig.update_layout(title_text='Accuracy (%) of Euclidean and Manhattan Implementations of <br> KNN on the Netflix Dataset using 2,135 Test Points and K = 10',
                  xaxis_title='Total Points Tested',
                  yaxis_title='Accuracy (%)')
# display the plot
fig.show()

