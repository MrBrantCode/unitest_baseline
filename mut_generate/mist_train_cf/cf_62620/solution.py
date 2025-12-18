"""
QUESTION:
Write a function to generate an ffmpeg command that converts an mkv video to avi format while decreasing the resolution from 4K to 1080p at 30 fps. The function should take input and output file names as parameters and return the ffmpeg command as a string.
"""

def generate_ffmpeg_command(input_file, output_file):
    """
    Generate an ffmpeg command that converts an mkv video to avi format 
    while decreasing the resolution from 4K to 1080p at 30 fps.

    Args:
        input_file (str): The name of the input file.
        output_file (str): The name of the output file.

    Returns:
        str: The ffmpeg command as a string.
    """
    return f"ffmpeg -i {input_file} -vf scale=-1:1080 -r 30 {output_file}"