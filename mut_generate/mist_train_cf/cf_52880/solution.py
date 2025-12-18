"""
QUESTION:
Create a function named `create_fruit_basket_svg` that generates an SVG markup for a basket filled with various fruits. The function should include the following features: 

* Each fruit should have unique colors, shadow effects, and textures, and should imitate the irregular shapes and textures of real fruits.
* The fruits should exhibit different stages of maturity symbolized by varying shades of their respective colors.
* The basket should be interactive, enabling a user to "pick" a fruit by clicking on it, resulting in its removal from the basket.
* The basket should have a capacity limit that can be adjusted, preventing additional fruits from being added until some are taken out.
* Each fruit should contribute a different weight, and the user should receive a notification when the weight limit is attained.
* The user should be able to sort the fruits based on their type, color, and weight, and view the total weight of the fruits in the basket.

Restrictions: The solution should not resemble perfect geometric figures and should be implemented using SVG.
"""

def create_fruit_basket_svg(fruits):
    svg = '<svg width="500" height="500">\n'
    svg += '<rect x="50" y="50" width="400" height="400" fill="#F5F5DC" rx="20" />\n'  # basket

    for i, fruit in enumerate(fruits):
        x = 100 + (i % 5) * 50
        y = 100 + (i // 5) * 50
        color = fruit['color']
        svg += f'<circle cx="{x}" cy="{y}" r="20" fill="{color}" />\n'  # fruit
        svg += f'<text x="{x}" y="{y+30}" text-anchor="middle" font-size="12">{fruit["name"]}</text>\n'

    svg += '</svg>'
    return svg

# Note: This function requires a list of dictionaries, where each dictionary represents a fruit with 'name' and 'color' keys.
# Example usage: fruits = [{'name': 'Apple', 'color': 'red'}, {'name': 'Banana', 'color': 'yellow'}, ...]