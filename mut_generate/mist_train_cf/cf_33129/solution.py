"""
QUESTION:
Implement a function `extract_features` that takes a string of HTML code for a navigation menu as input and returns a list of dictionaries, where each dictionary contains the feature name, URL, and icon (either Font Awesome class or image source) associated with each feature. The function should parse the HTML code to extract the feature details. 

The input HTML code is a string containing list items (`<li>`) with links and icons. Each link is generated using a template engine and the icons are displayed using Font Awesome classes or image sources. 

The output should be a list of dictionaries, where each dictionary contains the keys "feature", "link", and "icon".
"""

from typing import List, Dict
import re

def extract_features(html_code: str) -> List[Dict[str, str]]:
    features = []
    pattern = r'<li><a href="(.+?)".*?>(?:<img src="(.+?)".*?>|<i class="(.+?)"></i>)?\s*<span>(.+?)</span></a></li>'
    matches = re.findall(pattern, html_code)
    
    for match in matches:
        link, icon_img, icon_fa, feature = match
        icon = icon_img if icon_img else icon_fa
        features.append({"feature": feature, "link": link, "icon": icon})
    
    return features