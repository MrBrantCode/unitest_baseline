"""
QUESTION:
Create a function `send_message` that takes in a list of messages, a preferred language, a preferred tone, and an optional motivational parameter. The function should return a string containing the messages translated to the preferred language and formatted according to the preferred tone. 

The function should support two languages (English and Spanish) and three tones (Friendly, Formal, and Motivational). If the Motivational tone is selected, an uplifting message should be added to the end of the response. If the motivational parameter is True, an additional motivational message should be added to the end of the response. If the selected language or tone is not available, the function should return an error message.
"""

def send_message(messages, language='English', tone='Friendly', motivational=False):
    languages = ['English', 'Spanish']
    tones = ['Friendly', 'Formal', 'Motivational']

    if language not in languages:
        return "We're sorry, the language you selected is not available."

    if tone not in tones:
        return "We're sorry, the tone you selected is not available."

    if isinstance(messages, str):
        messages = [messages]

    response = ""
    for message in messages:
        if language == 'English':
            if tone == 'Friendly':
                response += f"{message}.\n"
            elif tone == 'Formal':
                response += f"{message}.\nPlease let us know if you have any further questions.\n"
            elif tone == 'Motivational':
                response += f"{message}.\nRemember to take care of yourself and believe in your abilities.\n"
        elif language == 'Spanish':
            if tone == 'Friendly':
                response += f"{message}.\n"
            elif tone == 'Formal':
                response += f"{message}.\nPor favor háganos saber si tiene alguna otra pregunta.\n"
            elif tone == 'Motivational':
                response += f"{message}.\nRecuerde cuidarse y creer en sus habilidades.\n"

    if motivational:
        response += "You are strong and capable, and we believe in you!"

    return response