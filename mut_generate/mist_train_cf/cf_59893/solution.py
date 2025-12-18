"""
QUESTION:
Construct two functions, `normalize_recursive` and `denormalize`, to normalize a given unidimensional numerical array to support a typical Gaussian distribution and then denormalize the normalized array back to its original form, respectively. The `normalize_recursive` function should utilize a recursive approach to compute the mean and standard deviation of the array and then normalize it by subtracting the mean and dividing by the standard deviation. The `denormalize` function should restore the normalized array back to its original form by multiplying with the standard deviation and adding the mean. Both functions should handle TypeError if the input is not a numerical list and use only built-in Python functionalities, without any external packages such as NumPy and SciPy.
"""

def mean_recursive(arr, index=0):
    n = len(arr)
    try:
        if index == n-1:
            return arr[index]/n
        else:
            return (arr[index]/n + mean_recursive(arr, index + 1))
    except TypeError:
        print("TypeError: Input should be a numerical list")
        return
    
def std_dev_recursive(arr, mean, index=0):
    n = len(arr)
    try:
        if index == n-1:
            return ((arr[index]-mean)**2)/n
        else:
            return ((arr[index]-mean)**2)/n + std_dev_recursive(arr, mean, index + 1)
    except TypeError:
        print("TypeError: Input should be a numerical list")
        return

def normalize_recursive(arr):
    mean = mean_recursive(arr)
    std_dev = std_dev_recursive(arr, mean)**0.5
    try:
        return [(x - mean)/std_dev for x in arr]
    except TypeError:
        print("TypeError: Input should be a numerical list")
        return

def denormalize(arr, original):
    original_mean = mean_recursive(original)
    original_std_dev = std_dev_recursive(original, original_mean)**0.5
    try:
        return [(x * original_std_dev) + original_mean for x in arr]
    except TypeError:
        print("TypeError: Input should be a numerical list")
        return