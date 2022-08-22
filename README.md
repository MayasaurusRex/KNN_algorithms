SUMMARY
==================================================================================

This file is created contains my implementation for the KNN algorithm for both 
the Iris dataset and the Netflix dataset.

The Iris dataset can be run on it's own, but please follow this order for
running the Netflix files:

    1. create_test_file.py                       -> run time ~= 2 minutes
    2. create_true_ratings_file.py               -> run time ~= 2 minutes
    3. knn_euclidean_ratings.py                  -> run time ~= 3 hours
    4. knn_manhattan_ratings.py                  -> run time ~= 3 hours
    5. knn_euclidean_manhattan_comparison.py     -> run time ~= 1 minute
    
My overall goals, comparisons of KNN implementations, and outcomes can be found in the 
attached report named "FinalReport.pdf"


ADDITIONAL NOTES ON THE NETFLIX DATASET
==================================================================================

The data for this project is included in the submission, and is from the 2006-2009 
Netflix challenge, which I was able to find online (and I'll add here for 
reference/sourcing): 
https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data

The Netlix_Prize_Instructions.txt file has more information reguarding the data
in these files, what they represent, and more information about the challenge.

I wanted to compare KNN implementations using Euclidean and Manhattan distance
calculations and did so by applying two different KNN algorithms with the same 
k value (k = 10). Then, I performed RMSE calculations to see how close the data
was to the prediction and also calculated the accuracy to see how many data    
points were exactly correct.

Additional information about the Netflix dataset can be found [here](
