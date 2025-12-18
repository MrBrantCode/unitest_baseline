"""
QUESTION:
Your task is to build a model^(1) which can predict y-coordinate.
You can pass tests if predicted y-coordinates are inside error margin.

You will receive train set which should be used to build a model. 
After you build a model tests will call function ```predict``` and pass x to it. 

Error is going to be calculated with RMSE.



Blocked libraries: sklearn, pandas, tensorflow, numpy, scipy

Explanation
[1] A mining model is created by applying an algorithm to data, but it is more than an algorithm or a metadata container: it is a set of data, statistics, and patterns that can be applied to new data to generate predictions and make inferences about relationships.
"""

def train_and_predict(train_set, x):
    """
    Trains a simple linear regression model using the provided train_set and predicts the y-coordinate for the given x.

    Parameters:
    - train_set (list of tuples): A list of (x, y) pairs used to train the model.
    - x (float): The x-coordinate for which the y-coordinate needs to be predicted.

    Returns:
    - float: The predicted y-coordinate.
    """
    sx = sy = sxx = sxy = 0
    n = len(train_set)
    
    for i in range(n):
        sx += train_set[i][0]
        sy += train_set[i][1]
        sxx += train_set[i][0] ** 2
        sxy += train_set[i][0] * train_set[i][1]
    
    b = (n * sxy - sx * sy) / (n * sxx - sx ** 2)
    a = (sy - b * sx) / n
    
    return a + b * x