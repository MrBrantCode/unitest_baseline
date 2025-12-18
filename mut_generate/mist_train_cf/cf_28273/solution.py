"""
QUESTION:
Create a function `get_top_labels(image, model, preprocess_input, decode_predictions)` that takes a NumPy array `image` representing the input image, a pre-trained deep learning model `model`, a function `preprocess_input` to preprocess the image, and a function `decode_predictions` to decode the model predictions. The function should preprocess the image, make predictions using the model, decode the predictions to obtain the top 10 human-readable labels, and return them as a list of tuples containing the label name and the associated prediction score.
"""

def entrance(image, model, preprocess_input, decode_predictions):
    # Expand dimensions of the input image
    expanded_image = np.expand_dims(image, axis=0)
    
    # Preprocess the expanded image
    preprocessed_image = preprocess_input(expanded_image)
    
    # Predict labels for the preprocessed image using the model
    predictions = model.predict(preprocessed_image)
    
    # Decode the predictions to obtain the top 10 labels
    top_labels = decode_predictions(predictions, top=10)
    
    return top_labels