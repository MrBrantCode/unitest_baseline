"""
QUESTION:
Write a function `decode_url(url)` that decodes a given URL encoded string, handling special characters including emojis and foreign characters, as well as decoding HTML entities. The function should not rely on external libraries or built-in functions specifically designed for URL decoding or HTML entity decoding.
"""

def decode_url(url):
    decoded_url = ""
    i = 0
    while i < len(url):
        if url[i] == "%":
            # URL encoded character
            hex_code = url[i+1:i+3]
            decoded_url += chr(int(hex_code, 16))
            i += 3
        elif url[i:i+2] == "&#":
            # HTML entity
            entity_end_index = url.find(";", i+2)
            entity = url[i+2:entity_end_index]
            if entity[0] == "x":
                decoded_url += chr(int(entity[1:], 16))
            else:
                decoded_url += chr(int(entity))
            i = entity_end_index + 1
        else:
            decoded_url += url[i]
            i += 1
    
    return decoded_url