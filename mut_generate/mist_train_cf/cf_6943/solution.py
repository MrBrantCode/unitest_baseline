"""
QUESTION:
Create a function named `translate(word)` that takes an English word or phrase as input and returns its translation in Spanish. The function should use a dictionary to store the translations for the following words and phrases: "Hello", "Thank You", "Goodbye", "Please", "Sorry", "Excuse me", "I'm sorry", "I don't understand", "How are you?", "Where is the nearest restaurant?", "What is your name?", "Can you help me?", "What time is it?", and "How much does it cost?". If the input word or phrase is not in the dictionary, the function should return the message "Translation not available".
"""

def translate(word):
    translations = {
        "Hello": "Hola",
        "Thank You": "Gracias",
        "Goodbye": "Adiós",
        "Please": "Por favor",
        "Sorry": "Perdón",
        "Excuse me": "Disculpe",
        "I'm sorry": "Lo siento",
        "I don't understand": "No entiendo",
        "How are you?": "¿Cómo estás?",
        "Where is the nearest restaurant?": "¿Dónde está el restaurante más cercano?",
        "What is your name?": "¿Cuál es tu nombre?",
        "Can you help me?": "¿Puedes ayudarme?",
        "What time is it?": "¿Qué hora es?",
        "How much does it cost?": "¿Cuánto cuesta?",
    }
    return translations.get(word, "Translation not available")