"""
QUESTION:
Implement the function `hyperparameter_tuning` that takes the following parameters: `df_full_train`, `y_full_train`, `df_test`, `y_test`, `inner_layers`, `droprate`, `learning_rate`, and `input_droprate`. The function should perform a grid search over the hyperparameters, train a neural network with each combination, and return the best set of hyperparameters as a dictionary containing the keys 'inner_layers', 'droprate', 'learning_rate', and 'input_droprate'. The function should use `train_NN` to train the neural network with the current hyperparameters. 

Restrictions:
- `inner_layers` is a list of integers representing the sizes of the inner layers of the neural network to be tuned
- `droprate`, `learning_rate`, and `input_droprate` are lists of floating-point values representing the dropout rates, learning rates, and input dropout rates to be tuned respectively
- `train_NN` is a function that trains a neural network with given hyperparameters and returns its accuracy.
"""

import itertools

def hyperparameter_tuning(df_full_train, y_full_train, df_test, y_test, inner_layers, droprate, learning_rate, input_droprate):
    best_hyperparameters = {}
    best_accuracy = 0.0

    # Perform grid search to find the best combination of hyperparameters
    for layers, dr, lr, input_dr in itertools.product(inner_layers, droprate, learning_rate, input_droprate):
        # Train neural network with current hyperparameters
        accuracy = train_NN(df_full_train, y_full_train, df_test, y_test,
                            inner_layers=layers, droprate=dr, learning_rate=lr, input_droprate=input_dr)

        # Update best hyperparameters if current accuracy is higher
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_hyperparameters['inner_layers'] = layers
            best_hyperparameters['droprate'] = dr
            best_hyperparameters['learning_rate'] = lr
            best_hyperparameters['input_droprate'] = input_dr

    return best_hyperparameters