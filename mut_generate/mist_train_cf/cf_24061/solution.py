"""
QUESTION:
Write a function called `predict_car_price` to estimate the price of a car based on its features. The function should take as input a dictionary or data structure containing the car's make, model, year, engine size, and condition, and return the predicted price.
"""

def predict_car_price(car_features):
    # For this example, let's assume we are using a linear regression model
    # We would need to train the model using a dataset of car features and prices
    # Here, we are just simulating the model for demonstration purposes
    price = 10000 + car_features['year'] * 1000 + car_features['engine_size'] * 500
    
    # Condition of the car affects the price, with 'new' being the most expensive
    if car_features['condition'] == 'new':
        price *= 1.2
    elif car_features['condition'] == 'used':
        price *= 0.8
    elif car_features['condition'] == 'old':
        price *= 0.5
        
    # Different makes and models have different base prices
    if car_features['make'] == 'Toyota' and car_features['model'] == 'Camry':
        price += 5000
    elif car_features['make'] == 'Honda' and car_features['model'] == 'Civic':
        price += 4000
        
    return price