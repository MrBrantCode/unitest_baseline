"""
QUESTION:
Create a function `preprocess_image_data` that takes in the training image dataset `x_train`, training labels `y_train`, testing image dataset `x_test`, and testing labels `y_test`. The function should reshape the images in the datasets to have a shape of (number of samples, 784), convert the data type of the images from uint8 to float32, and normalize the pixel values by dividing them by 255. The function should return the preprocessed training and testing datasets.
"""

def preprocess_image_data(x_train, y_train, x_test, y_test):
    # Reshape the images and convert data type
    x_train = x_train.reshape(x_train.shape[0], 784).astype("float32") / 255
    x_test = x_test.reshape(x_test.shape[0], 784).astype("float32") / 255
    return x_train, y_train, x_test, y_test