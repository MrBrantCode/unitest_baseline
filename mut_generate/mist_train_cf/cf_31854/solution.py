"""
QUESTION:
Implement the `predict` method of the `CustomModel` class to handle the case when the model is trained and is a one-class classification model. The method should take a feature matrix `X` as input and return the predictions. Assume that `self.trained` is a boolean indicating whether the model is trained, `self.oneclass` is a boolean indicating whether it is a one-class classification model, and `self.learner` is the trained model. The `predict` method should return a numpy array of predictions. The method should also include an assertion to check if the model is trained before making predictions.
"""

def predict(self, X): 
    assert (self.trained == True), "Must call fit first!"
    if self.oneclass == False:
        tmp_pred = self.learner.predict(X).reshape(-1)
    else:
        # Populate tmp_pred with a default value for the one-class classification scenario
        tmp_pred = np.zeros((X.shape[0]))
    return tmp_pred