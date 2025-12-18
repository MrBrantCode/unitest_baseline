"""
QUESTION:
Create a function named `generate_birthday_messages` that takes a list of friend names as input and returns a list of personalized birthday messages. Each message should include the friend's name and reflect their individuality, interests, or traits. If the friend's name is not recognized, a default birthday message should be used.
"""

def generate_birthday_messages(friends):
    messages = []
    for friend in friends:
        # Add your personalized messages for each friend here
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