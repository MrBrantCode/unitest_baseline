"""
QUESTION:
Create a function named `birthday_wishes` that generates a personalized birthday message for an animal lover. The function should take two parameters: `name` (the person's name) and `animal` (their favorite animal). The message should include a cute image of the animal using HTML tags. If the animal is not supported, return an error message.
"""

def birthday_wishes(name, animal):
    # Define a dictionary with images of animals
    animal_images = {
        'cat': 'https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_960_720.jpg',
        'dog': 'https://cdn.pixabay.com/photo/2016/02/19/15/46/dog-1210559_960_720.jpg',
        'rabbit': 'https://cdn.pixabay.com/photo/2018/04/03/21/25/rabbit-3283016_960_720.jpg',
        'hamster': 'https://cdn.pixabay.com/photo/2016/01/19/18/03/hamster-1150110_960_720.jpg',
        'bird': 'https://cdn.pixabay.com/photo/2018/03/12/12/32/bird-3210266_960_720.jpg'
    }
    
    # Check if the animal is in the dictionary
    if animal not in animal_images:
        return "Sorry, we don't have an image for that animal."
    
    # Create the birthday message with the animal image
    message = f"Happy birthday, {name}! Wishing you a wonderful day filled with joy and happiness. Here's a cute {animal} to brighten up your day: <br> <img src='{animal_images[animal]}' width='300' height='200'>"
    
    return message