"""
QUESTION:
Design a function `generate_message(weather, time_of_day)` that takes two strings as inputs, `weather` and `time_of_day`, and returns a string message based on the given rules. The function should handle invalid inputs and provide a default message for weather conditions or times of day not covered in the rules. The rules are as follows:

- If the weather is sunny and it's morning, return "It's a great day to stay outside! Enjoy the morning sun!"
- If the weather is sunny and it's afternoon, return "It's a great day to stay outside! Don't forget your sunscreen!"
- If the weather is sunny and it's evening, return "It's a great day to stay outside! Enjoy the sunset!"
- If the weather is cloudy and it's morning, return "Stay indoors and enjoy the clouds! It's a cozy morning."
- If the weather is cloudy and it's afternoon, return "Stay indoors and enjoy the clouds! Perfect time for a nap."
- If the weather is cloudy and it's evening, return "Stay indoors and enjoy the clouds! It's a peaceful evening."

The function should return an error message if the weather is neither sunny nor cloudy, or if the time of day is not morning, afternoon, or evening.
"""

def generate_message(weather, time_of_day):
    try:
        if weather.lower() == 'sunny':
            if time_of_day.lower() == 'morning':
                return "It's a great day to stay outside! Enjoy the morning sun!"
            elif time_of_day.lower() == 'afternoon':
                return "It's a great day to stay outside! Don't forget your sunscreen!"
            elif time_of_day.lower() == 'evening':
                return "It's a great day to stay outside! Enjoy the sunset!"
            else:
                return "Invalid time of day. Please input either morning, afternoon, or evening."

        elif weather.lower() == 'cloudy':
            if time_of_day.lower() == 'morning':
                return "Stay indoors and enjoy the clouds! It's a cozy morning."
            elif time_of_day.lower() == 'afternoon':
                return "Stay indoors and enjoy the clouds! Perfect time for a nap."
            elif time_of_day.lower() == 'evening':
                return "Stay indoors and enjoy the clouds! It's a peaceful evening."
            else:
                return "Invalid time of day. Please input either morning, afternoon, or evening."

        else:
            return "Invalid weather condition. Please input either sunny or cloudy."

    except Exception:
        return "Invalid input given. Please enter valid weather condition (sunny/ cloudy) and time of day (morning/afternoon/evening)."