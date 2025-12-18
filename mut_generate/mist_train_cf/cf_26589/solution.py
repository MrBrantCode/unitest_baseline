"""
QUESTION:
Implement the ASAPBuilder class with an initializer and a Build method. The initializer should take four parameters: corner, top, side, and figures. The Build method should assemble the figures using the available pieces from the corner, top, and side lists and return the updated model. Each figure in the figures list is a dictionary with a "type" key that can have the values "corner", "top", or "side". If a figure's type matches a piece type and a piece of that type is available, add the piece to the model and remove it from its respective list.
"""

def build_asap_builder(corner, top, side, figures):
    model = []
    for figure in figures:
        if figure["type"] == "corner" and corner:
            model.append(corner.pop(0))
        elif figure["type"] == "top" and top:
            model.append(top.pop(0))
        elif figure["type"] == "side" and side:
            model.append(side.pop(0))
    return model