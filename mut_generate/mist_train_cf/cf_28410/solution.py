"""
QUESTION:
Create a function called `minibatches` that takes two parameters: `data` and `minibatchSize`. The `data` parameter is a list of tuples, where each tuple contains a sequence of words and its corresponding label. The `minibatchSize` parameter is an integer representing the size of each minibatch. The function should create minibatches of the specified size from the given data, where each minibatch consists of input sequences and their corresponding labels, and return the minibatches.
"""

def minibatches(data, minibatchSize):
    x_batch, y_batch = [], []
    for i in range(0, len(data), minibatchSize):
        batch = data[i:i + minibatchSize]
        x_batch.append([item[0] for item in batch])  
        y_batch.append([item[1] for item in batch])  
    return x_batch, y_batch