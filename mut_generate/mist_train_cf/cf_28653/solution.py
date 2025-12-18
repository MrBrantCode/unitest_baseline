"""
QUESTION:
Implement the function `process_sdp_attributes(sdp_attributes: List[str]) -> List[str]` that takes a list of strings representing WebRTC SDP attributes as input and returns a new list of strings after processing the SDP attributes. Each SDP attribute is in the format "attribute=value" and may have leading or trailing whitespace. The function should remove any leading or trailing whitespace from each attribute, convert all attribute names to lowercase, and remove any duplicate attributes, keeping only the first occurrence of each attribute.
"""

from typing import List

def process_sdp_attributes(sdp_attributes: List[str]) -> List[str]:
    processed_attributes = []
    seen_attributes = set()
    
    for attribute in sdp_attributes:
        attribute = attribute.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
        attribute_name = attribute.split('=')[0]  # Extract attribute name
        
        if attribute_name not in seen_attributes:
            processed_attributes.append(attribute)
            seen_attributes.add(attribute_name)
    
    return processed_attributes