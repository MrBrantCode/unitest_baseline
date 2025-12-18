"""
QUESTION:
Write a function `generate_button_code` that generates code to create buttons with specified properties. The function should take the following parameters: 
- `button_labels`: A list of strings representing the labels for the buttons.
- `bg_colors`: A list of strings representing the background colors for the buttons.
- `text_colors`: A list of strings representing the text colors for the buttons.
- `fonts`: A list of strings representing the fonts for the buttons.
- `grid_positions`: A list of tuples representing the grid positions for the buttons in the format (row, column).
- `command_functions`: A list of strings representing the command functions associated with each button.
 
The function should return a string containing the code snippet for creating the buttons based on the input parameters.
"""

def generate_button_code(button_labels, bg_colors, text_colors, fonts, grid_positions, command_functions):
    code = "from tkinter import Button\n\n"
    for label, bg, text_color, font, position, command in zip(button_labels, bg_colors, text_colors, fonts, grid_positions, command_functions):
        code += f"{label.lower().replace(' ', '_')} = Button(gkf.topFrame, text=\"{label}\", bg=\"{bg}\", fg=\"{text_color}\", font=(\"{font}\", 12), highlightthickness=1, highlightbackground=\"{text_color}\", command=gkf.{command})\n"
        code += f"{label.lower().replace(' ', '_')}.grid(row={position[0]}, column={position[1]}, padx=5, pady=5)\n\n"
    return code