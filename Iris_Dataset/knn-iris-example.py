# The purpose of this algorithm implementation is to gain
# a better understanding of the algorithm before
# implementing it in the Netflix dataset

# import libraries
from csv import reader
from math import sqrt
 
# Load a CSV file
def load_csv(filename):
	data = list() # list to store the data points
	with open(filename, 'r') as file: # open file
		csv_reader = reader(file) # read file
		for row in csv_reader: # iterate through file rows
			if not row:
				continue
			data.append(row) # append data to list object
	return data # return the data
 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0 
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2 # euclidean formula
	return sqrt(distance)
 
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	# sort the distances
	distances.sort(key=lambda asc: asc[1])
	# get the k nearest neighbors
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	# print(neighbors)
	return neighbors
 
# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	# get the k nearest neighbors
	neighbors = get_neighbors(train, test_row, num_neighbors)
	# see the neighbor's classifications
	output_values = [row[-1] for row in neighbors]
	# perform the majority vote to predict the perdiction
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
# Make a prediction with KNN on Iris Dataset
filename = 'iris.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# define model parameter
num_neighbors = 6
# define a new record
    # Sepal length in cm.
    # Sepal width in cm.
    # Petal length in cm.
    # Petal width in cm.

row = [5.2,2.4,3.2,2.3] # versicolor
# predict the label
label = predict_classification(dataset, row, num_neighbors)
print('Data=%s, Predicted: %s' % (row, label))

row = [5.2,3.4,1.2,0.3] # setosa
# predict the label
label = predict_classification(dataset, row, num_neighbors)
print('Data=%s, Predicted: %s' % (row, label))

row = [6.4,3.7,5.3,2.1] # virginica
# predict the label
label = predict_classification(dataset, row, num_neighbors)
print('Data=%s, Predicted: %s' % (row, label))