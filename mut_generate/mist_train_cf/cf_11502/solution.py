"""
QUESTION:
Create a function `Button` that renders a button with a specified label, initial background color, hover background color, and click background color. The button should have the following features:
- When clicked, the background color changes and a counter increases by 1, displayed next to the button.
- A hover effect changes the background color when the mouse hovers over the button.
- The button has a disabled state where it cannot be clicked.
- The button has a tooltip that displays a specified message when hovered over.
- The button has a loading state where it shows a loading spinner instead of the text label.

The function should take the following parameters: 
- `label`: The text label of the button.
- `initialBackgroundColor`: The initial background color of the button.
- `hoverBackgroundColor`: The background color of the button when hovered over.
- `clickBackgroundColor`: The background color of the button when clicked.
- `disabled`: A boolean indicating whether the button is disabled.
- `tooltipMessage`: The message to be displayed in the tooltip.
"""

def Button(label, initialBackgroundColor, hoverBackgroundColor, clickBackgroundColor, disabled=False, tooltipMessage=""):
    # This is a simplified implementation of the Button function in Python
    # It does not render a GUI but instead returns a string representation of the button
    # The actual implementation would require a GUI library such as Tkinter or PyQt

    return f"""
    Button(label={label}, 
           initialBackgroundColor={initialBackgroundColor}, 
           hoverBackgroundColor={hoverBackgroundColor}, 
           clickBackgroundColor={clickBackgroundColor}, 
           disabled={disabled}, 
           tooltipMessage={tooltipMessage})
    """