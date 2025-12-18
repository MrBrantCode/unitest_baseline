"""
QUESTION:
Implement a function `data_splitting` that takes a float `train_frac` and a list of integers `Num_Each_Class` as input. The function should calculate the number of samples for training and testing for each class based on `train_frac` and `Num_Each_Class`. It should then return a tuple containing four lists: `Train_Patch` (training samples for each class), `Train_Label` (corresponding training labels for each class), `Test_Patch` (testing samples for each class), and `Test_Label` (corresponding testing labels for each class).
"""

import math
import numpy as np

def data_splitting(train_frac, Num_Each_Class):
    Num_Train_Each_Class = [math.ceil(train_frac * x) for x in Num_Each_Class]
    Num_Train_Each_Class = [int(x) for x in Num_Train_Each_Class]
    
    Num_Test_Each_Class = list(np.array(Num_Each_Class) - np.array(Num_Train_Each_Class))
    
    Train_Patch, Train_Label, Test_Patch, Test_Label = [], [], [], []
    
    # Split the dataset into training and testing sets for each class
    for i in range(len(Num_Each_Class)):
        # Generate training samples and labels
        train_samples = [f"Class {i+1} Sample {j+1}" for j in range(Num_Train_Each_Class[i])]
        train_labels = [f"Class {i+1}" for _ in range(Num_Train_Each_Class[i])]
        
        # Generate testing samples and labels
        test_samples = [f"Class {i+1} Sample {j+1}" for j in range(Num_Train_Each_Class[i], Num_Each_Class[i])]
        test_labels = [f"Class {i+1}" for _ in range(Num_Test_Each_Class[i])]
        
        # Append the samples and labels to the respective lists
        Train_Patch.extend(train_samples)
        Train_Label.extend(train_labels)
        Test_Patch.extend(test_samples)
        Test_Label.extend(test_labels)
    
    return Train_Patch, Train_Label, Test_Patch, Test_Label