"""
QUESTION:
Implement the `SimpleLinearRegression` class with methods to fit a linear regression model to a given dataset and make predictions based on the learned parameters. The class should have the following properties and methods:

- `slope` and `intercept` attributes, initialized to `None`
- `fit(X, y)` method, which calculates the slope and intercept using the least squares method
- `predict(X)` method, which takes in a single input value or a list/numpy array of values and returns the predicted output value(s)

The slope and intercept should be calculated using the following formulae:
- Slope (m) = Σ((x - mean(x)) * (y - mean(y))) / Σ((x - mean(x))^2)
- Intercept (c) = mean(y) - m * mean(x)
"""

def simple_linear_regression(X, y):
    mean_x = sum(X) / len(X)
    mean_y = sum(y) / len(y)
    numerator = sum((x - mean_x) * (y_i - mean_y) for x, y_i in zip(X, y))
    denominator = sum((x - mean_x) ** 2 for x in X)
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    
    def predict(X):
        if isinstance(X, (int, float)):
            return slope * X + intercept
        else:
            return [slope * x + intercept for x in X]
    
    return predict