"""
QUESTION:
Create a `send_message` function that accepts multiple messages, a preferred language, and a tone. The function should support English and Spanish languages, and three tones: Friendly, Formal, and Motivational. The Motivational tone adds an uplifting message to the end of the response. The function should return a string containing all messages with the selected language and tone. If the user selects the Motivational tone and passes `motivational=True`, an additional motivational message should be appended to the end of the response. If an invalid language or tone is selected, the function should return an error message.
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