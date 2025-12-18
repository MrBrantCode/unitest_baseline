"""
QUESTION:
Write a function `format_quiz(quiz)` that takes a JSON object representing a quiz as input. The JSON object has a list of questions, where each question contains a prompt, a list of options, and the correct answer index. The function should return a formatted string representing the quiz in a human-readable format with each question numbered and options labeled with letters.
"""

def entrance(quiz):
    formatted_quiz = ""
    for i, question in enumerate(quiz["questions"]):
        formatted_quiz += f"Question {i+1}: {question['prompt']}\n"
        for j, option in enumerate(question["options"]):
            formatted_quiz += f"    {chr(97+j)}) {option}\n"
    return formatted_quiz