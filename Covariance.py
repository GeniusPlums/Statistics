import numpy as np

# Define two lists of numbers
list1 = np.array([5, 7, 12, 8, 13])
list2 = np.array([4, 6, 10, 12, 8])

# Calculate the covariance
covariance_matrix = np.cov(list1, list2)

# Extract the covariance from the matrix
covariance = covariance_matrix[0, 1]

print("Covariance: ", covariance)