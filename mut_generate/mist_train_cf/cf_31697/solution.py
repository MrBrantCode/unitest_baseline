"""
QUESTION:
Implement the function `process_command(command)` that processes the given commands and performs the corresponding actions for managing FAQs and presentations in a group chat application. The function takes a string `command` as input, where the command format determines the action to be performed. 

The function should support the following commands:
- `{0} {room_number} {url} {presentation_title}`: Add a presentation with a notification in a specific room.
- `{5} {room_number} {faq_content}`: Manually insert a FAQ in a specific room.
- `{8} {5}`: List all FAQs in every room.
- `{1} {question_number} {answer_content}`: Answer a specific FAQ.
- `delete faq {faq_thread_number}`: Delete a FAQ thread, including the answer, comments, and related messages.

Return a string indicating the result of the action or an error message if the command is invalid.
"""

def process_command(command):
    if command.startswith("{0}"):
        parts = command.split()
        if len(parts) != 4:
            return "Invalid command format"
        _, room_number, url, presentation_title = parts
        # Perform the action to add presentation with notification
        return f"Presentation '{presentation_title}' added to room {room_number} with URL {url}"
    
    elif command.startswith("{5}"):
        parts = command.split()
        if len(parts) != 3:
            return "Invalid command format"
        _, room_number, faq_content = parts
        # Perform the action to manually insert FAQ
        return f"FAQ '{faq_content}' added to room {room_number}"
    
    elif command.startswith("{8} {5}"):
        # Perform the action to list all FAQs in every room
        return "List of FAQs in every room"
    
    elif command.startswith("{1}"):
        parts = command.split()
        if len(parts) != 3:
            return "Invalid command format"
        _, question_number, answer_content = parts
        # Perform the action to answer a specific FAQ
        return f"FAQ {question_number} answered: {answer_content}"
    
    elif command.startswith("delete faq"):
        parts = command.split()
        if len(parts) != 3:
            return "Invalid command format"
        _, _, faq_thread_number = parts
        # Perform the action to delete a FAQ thread
        return f"FAQ thread {faq_thread_number} deleted"
    
    else:
        return "Invalid command format"