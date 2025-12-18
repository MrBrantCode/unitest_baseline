"""
QUESTION:
Implement a function `embed_data_in_audio` to hide a secret message within an audio signal using the Least Significant Bit (LSB) steganography technique. The function should take two parameters: `audio_signal` (a list of integers representing the audio data) and `secret_message` (a string representing the message to be hidden). The function should return the modified audio signal with the secret message embedded. The embedding process should be done by replacing the least significant bit of each audio sample with the corresponding bit of the secret message.
"""

def embed_data_in_audio(audio_signal, secret_message):
    """
    Embed a secret message within an audio signal using the Least Significant Bit (LSB) steganography technique.

    Parameters:
    audio_signal (list): A list of integers representing the audio data.
    secret_message (str): A string representing the message to be hidden.

    Returns:
    list: The modified audio signal with the secret message embedded.
    """
    # Convert the secret message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

    # Initialize an empty list to store the modified audio signal
    modified_signal = []

    # Initialize a counter to keep track of the current bit in the binary message
    bit_index = 0

    # Iterate over the audio signal
    for sample in audio_signal:
        # If there are still bits left in the binary message
        if bit_index < len(binary_message):
            # Get the least significant bit of the current sample
            lsb = sample & 1

            # Get the current bit from the binary message
            bit = int(binary_message[bit_index])

            # Replace the least significant bit of the sample with the current bit
            modified_sample = (sample & ~1) | bit

            # Append the modified sample to the modified audio signal
            modified_signal.append(modified_sample)

            # Increment the bit index
            bit_index += 1
        else:
            # If there are no more bits left in the binary message, append the original sample
            modified_signal.append(sample)

    return modified_signal