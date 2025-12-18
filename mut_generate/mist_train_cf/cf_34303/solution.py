"""
QUESTION:
Implement a function `processInput(input: str) -> str` that takes a user input as a string and returns a corresponding response based on predefined rules. The function should match the input against a set of predefined strings and return the corresponding message if found. If the input does not match any predefined strings, the function should return a default message: "I'm sorry, I didn't understand that. Please try again." 

The predefined strings and their corresponding responses are:
- "stats1": "Where do you want to consult the statistics?"
- "statsaddr": "My Addresses"
- "statsp2m": "EqualHash"
- "statsReturn": "<< Back to Stats"
- "noneAddr": "You have not added an address yet.\nYou can use the /newaddr command to add a new address."
- "selectAddr": "Choose an address from the list below:"
- "noStats": "I'm sorry but there's still no information for this address. Try it later."
- "return": "<< Return"
- "viewAddr": "Here it is:\n   - Name: *<NAMEADDRESS>*\n   - Address: *<ADDRESS>*\n\nWhat do you want to do with the address?"
- "viewStats": "See stats"
"""

def processInput(input: str) -> str:
    predefined_responses = {
        "stats1": "Where do you want to consult the statistics?",
        "statsaddr": "My Addresses",
        "statsp2m": "EqualHash",
        "statsReturn": "<< Back to Stats",
        "noneAddr": "You have not added an address yet.\nYou can use the /newaddr command to add a new address.",
        "selectAddr": "Choose an address from the list below:",
        "noStats": "I'm sorry but there's still no information for this address. Try it later.",
        "return": "<< Return",
        "viewAddr": "Here it is:\n   - Name: *<NAMEADDRESS>*\n   - Address: *<ADDRESS>*\n\nWhat do you want to do with the address?",
        "viewStats": "See stats"
    }
    
    return predefined_responses.get(input, "I'm sorry, I didn't understand that. Please try again.")