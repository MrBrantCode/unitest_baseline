"""
QUESTION:
Create a Python function `generate_birthday_messages` that takes a list of friends' names as input and returns a list of personalized birthday messages. Each message should be unique to the corresponding friend and reflect their individuality, interests, and traits. Assume that the function will be provided with a predefined list of friends and their corresponding personalized messages.
"""

def generate_birthday_messages(friends):
    messages = []
    for friend in friends:
        if friend == "Emma":
            message = f"Happy birthday, {friend}! May your artistic skills blossom and bring you endless inspiration!"
        elif friend == "Sophia":
            message = f"Dear {friend}, I hope your birthday is filled with the sweetness of your favorite desserts and the warmth of your loved ones!"
        elif friend == "Jackson":
            message = f"Happy birthday, {friend}! May your adventurous spirit lead you to new and exciting places!"
        elif friend == "Aiden":
            message = f"Dear {friend}, I hope your birthday is as energetic and playful as you are!"
        elif friend == "Olivia":
            message = f"Happy birthday, {friend}! May your love for books and learning continue to inspire you!"
        elif friend == "Lucas":
            message = f"Dear {friend}, I hope your birthday is filled with laughter and joy, just like your infectious sense of humor!"
        elif friend == "Liam":
            message = f"Happy birthday, {friend}! May your love for music continue to move and inspire you!"
        elif friend == "Mia":
            message = f"Dear {friend}, I hope your birthday is as sweet and kind as you are!"
        elif friend == "Ava":
            message = f"Happy birthday, {friend}! May your creativity and imagination continue to flourish and amaze us all!"
        elif friend == "Noah":
            message = f"Dear {friend}, I hope your birthday is filled with adventure and excitement, just like your bold and fearless spirit!"
        else:
            message = f"Happy birthday, {friend}!"
        messages.append(message)
    return messages