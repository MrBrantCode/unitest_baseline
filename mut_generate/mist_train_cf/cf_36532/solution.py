"""
QUESTION:
Write a function `categorize_tags(tags)` that takes a list of accessory tags as input and returns a dictionary containing the count of each tag type, where the tag types are "clothing", "jewelry", "shoes", or "other". The function should categorize each tag based on the following rules: 
- "clothing" includes "hat", "scarf", "gloves", "belt", and "socks", 
- "jewelry" includes "bracelet", "earrings", and "necklace", 
- "shoes" includes only "shoes", 
- and any other tag is categorized as "other".
"""

def categorize_tags(tags):
    tag_counts = {
        "clothing": 0,
        "jewelry": 0,
        "shoes": 0,
        "other": 0
    }

    clothing_tags = ["hat", "scarf", "gloves", "belt", "socks"]
    jewelry_tags = ["bracelet", "earrings", "necklace"]

    for tag in tags:
        if tag in clothing_tags:
            tag_counts["clothing"] += 1
        elif tag in jewelry_tags:
            tag_counts["jewelry"] += 1
        elif tag == "shoes":
            tag_counts["shoes"] += 1
        else:
            tag_counts["other"] += 1

    return tag_counts