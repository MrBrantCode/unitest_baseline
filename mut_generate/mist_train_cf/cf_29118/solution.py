"""
QUESTION:
Create a function `prompt_yes_no` that takes a string prompt message as input and prompts the user to input a "yes" or "no" response. The function should return 0 for "yes", 1 for "no", and -1 if the user interrupts the input process with a keyboard interrupt. The function should handle invalid inputs by continuously prompting the user until a valid input is received.
"""

def prompt_yes_no(prompt_msg: str) -> int:
    try:
        yn = input(prompt_msg + " (y/n) ").lower()
        while yn not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            yn = input(prompt_msg + " (y/n) ").lower()
        
        return 0 if yn == 'y' else 1

    except KeyboardInterrupt:
        print("\nUser interrupted the input process.")
        return -1