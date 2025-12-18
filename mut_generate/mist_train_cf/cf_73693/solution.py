"""
QUESTION:
Develop a function to manage data of multiple individuals. The data for each individual should be stored in a dictionary with keys "name", "occupation", "birthday", and "hobby". 

The function should be able to add new data entries, update existing data, and view data for an individual. When adding or updating data, the function should check if the inputted name already exists. 

When viewing data, the function should calculate the age of the individual from their birthday and display it. If the individual's birthday for the current year has passed, the function should also display "Belated Happy Birthday!" The birthday should be inputted in a format that can be converted to a date.
"""

import datetime

def manage_data(data, action, name=None, occupation=None, birthday=None, hobby=None):
    """
    Manage data of multiple individuals.

    Args:
    - data (dict): Dictionary to store individual data.
    - action (str): Action to perform. Can be 'A' to add, 'U' to update, or 'V' to view.
    - name (str): Name of the individual.
    - occupation (str): Occupation of the individual.
    - birthday (str): Birthday of the individual in DD/MM/YYYY format.
    - hobby (str): Hobby of the individual.

    Returns:
    - data (dict): Updated dictionary with individual data.
    """

    if action.lower() == 'a':
        # Add new entry
        if name in data:
            print("Name already exists. Please update instead.")
            return data
        data[name] = {"name": name, "occupation": occupation, 
                      "birthday": datetime.datetime.strptime(birthday, "%d/%m/%Y").date(), 
                      "hobby": hobby}

    elif action.lower() == 'u':
        # Update existing entry
        if name not in data:
            print("No such person exists in the data.")
            return data
        data[name] = {"name": name, "occupation": occupation, 
                      "birthday": datetime.datetime.strptime(birthday, "%d/%m/%Y").date(), 
                      "hobby": hobby}

    elif action.lower() == 'v':
        # View entry
        if name not in data:
            print("No such person exists in the data.")
            return data
        age = datetime.date.today().year - data[name]['birthday'].year - ((datetime.date.today().month, datetime.date.today().day) < (data[name]['birthday'].month, data[name]['birthday'].day))
        print(f"Name: {data[name]['name']}")
        print(f"Occupation: {data[name]['occupation']}")
        print(f"Birthday: {data[name]['birthday']}")
        print(f"Age: {age}")
        print(f"Hobby: {data[name]['hobby']}")
        if data[name]['birthday'].replace(year=datetime.datetime.now().year) < datetime.date.today():
            print("Belated Happy Birthday!")

    return data