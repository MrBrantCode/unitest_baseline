"""
QUESTION:
Design an advanced watermarking system using Python and the PyCrypto toolkit, integrated within a Django web application, to ensure imperceptibility and security of real-time video-based data communication stored in a PostgreSQL relational database management system. The system should thwart unauthorized detection and potential data leaks, and be robust against advanced watermark detection attacks.
"""

def watermark_data(data, watermark):
    """
    Embeds a watermark into the given data using least significant bit coding.

    Args:
        data (str): The input data to be watermarked.
        watermark (str): The watermark to be embedded.

    Returns:
        str: The watermarked data.
    """
    # Convert data and watermark to binary
    data_binary = ''.join(format(ord(i), '08b') for i in data)
    watermark_binary = ''.join(format(ord(i), '08b') for i in watermark)

    # Calculate the length of the watermark
    watermark_length = len(watermark_binary)

    # Initialize the watermarked data
    watermarked_data = ''

    # Iterate over the data and embed the watermark
    for i in range(len(data_binary)):
        if i < watermark_length:
            # Embed the watermark bit into the least significant bit of the data
            watermarked_data += data_binary[i][:-1] + watermark_binary[i]
        else:
            # If the watermark is exhausted, just append the data as it is
            watermarked_data += data_binary[i]

    return watermarked_data