"""
QUESTION:
Write a function `parse_svg` that takes a string of SVG code as input and returns a structured representation of the extracted information about the linear gradients and the clip path.

The function should extract the following information:
- The IDs of all the linear gradients defined in the SVG code.
- The coordinates and gradient units (if specified) for each linear gradient.
- The ID and dimensions of the clip path, if present.

The function should be able to handle SVG code with different linear gradients and clip paths.
"""

import xml.etree.ElementTree as ET

def parse_svg(svg_code):
    root = ET.fromstring(svg_code)
    
    linear_gradients = root.findall('.//linearGradient')
    clip_paths = root.findall('.//clipPath')
    
    result = {
        "Linear Gradients": [],
        "Clip Path": None
    }
    
    for gradient in linear_gradients:
        gradient_info = {"ID": gradient.get("id")}
        stops = gradient.findall('.//stop')
        if stops:
            gradient_info["Stops"] = []
            for stop in stops:
                stop_info = {
                    "stop-color": stop.get("style").split(";")[0].split(":")[1],
                    "stop-opacity": stop.get("style").split(";")[1].split(":")[1],
                    "offset": stop.get("offset"),
                    "id": stop.get("id")
                }
                gradient_info["Stops"].append(stop_info)
        else:
            gradient_info["Coordinates"] = {
                "x1": gradient.get("x1"),
                "y1": gradient.get("y1"),
                "x2": gradient.get("x2"),
                "y2": gradient.get("y2")
            }
            gradient_info["Gradient Units"] = gradient.get("gradientUnits")
        
        result["Linear Gradients"].append(gradient_info)
    
    if clip_paths:
        clip_path_info = {
            "ID": clip_paths[0].get("id"),
            "Dimensions": {
                "x": clip_paths[0][0].get("x"),
                "y": clip_paths[0][0].get("y"),
                "width": clip_paths[0][0].get("width"),
                "height": clip_paths[0][0].get("height")
            }
        }
        result["Clip Path"] = clip_path_info
    
    return result