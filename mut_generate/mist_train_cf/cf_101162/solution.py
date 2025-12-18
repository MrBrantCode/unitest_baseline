"""
QUESTION:
Write a function called `enigma` that accepts four arguments: `characters`, `start_positions`, `offsets`, and `plugboard_connections`. The function should encrypt/decrypt the `characters` string based on the given Enigma machine settings. The function should return the encrypted/decrypted text.

`characters` is the character vector to be encrypted/decrypted. `start_positions` is a list of three integers representing the starting position of each wheel. `offsets` is a list of three integers representing the offset of each wheel after each character is encoded/decoded. `plugboard_connections` is a list of 20 tuples representing the connections made on the plugboard, where each tuple consists of two characters that are connected.

The function should work with all visible ASCII characters from space to ~ (ASCII codes 32 through 126). If the wheel goes past its limit, it should wrap around. The plugboard connections should be applied after the rotors.
"""

def enigma(characters, start_positions, offsets, plugboard_connections):
    # Convert plugboard connections to a dictionary
    plugboard_dict = {}
    for connection in plugboard_connections:
        plugboard_dict[connection[0]] = connection[1]
        plugboard_dict[connection[1]] = connection[0]
    
    # Initialize variables
    wheel_positions = start_positions.copy()
    coded = ""
    
    # Loop through each character in the input string
    for char in characters:
        # Convert character to ASCII code and shift by wheel positions
        code = ord(char) - 32
        code = (code + wheel_positions[2]) % 94
        code = (code + wheel_positions[1]) % 94
        code = (code + wheel_positions[0]) % 94
        
        # Apply plugboard connections if necessary
        if char in plugboard_dict:
            code = ord(plugboard_dict[char]) - 32
        
        # Shift by wheel offsets and convert back to character
        code = (code - wheel_positions[0]) % 94
        code = (code - wheel_positions[1]) % 94
        code = (code - wheel_positions[2]) % 94
        coded += chr(code + 32)
        
        # Update wheel positions
        wheel_positions[0] = (wheel_positions[0] + offsets[0]) % 94
        if wheel_positions[0] == start_positions[0]:
            wheel_positions[1] = (wheel_positions[1] + offsets[1]) % 94
            if wheel_positions[1] == start_positions[1]:
                wheel_positions[2] = (wheel_positions[2] + offsets[2]) % 94
    
    return coded