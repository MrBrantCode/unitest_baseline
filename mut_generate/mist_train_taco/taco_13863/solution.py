"""
QUESTION:
*Are you a file extension master? Let's find out by checking if Bill's files are images or audio files. Please use regex if available natively for your language.*

You will create 2 string methods:

- **isAudio/is_audio**, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .mp3, .flac, .alac, or .aac.

- **isImage/is_image**, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .jpg, .jpeg, .png, .bmp, or .gif. 


*Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only*

**Rules**

1. It should return true or false, simply.
2. File extensions should consist of lowercase letters and numbers only.
3. File names should consist of letters only (uppercase, lowercase, or both)

Good luck!
"""

def check_file_type(filename):
    """
    Determines if the given filename corresponds to an audio or image file based on its extension.

    Parameters:
    filename (str): The name of the file to be checked, including the extension.

    Returns:
    str: A string indicating the type of the file. Possible values are "audio", "image", or "unknown".
    """
    try:
        (name, ext) = filename.split('.')
    except ValueError:
        return "unknown"
    
    if name.isalpha():
        if ext in {'mp3', 'flac', 'alac', 'aac'}:
            return "audio"
        elif ext in {'jpg', 'jpeg', 'png', 'bmp', 'gif'}:
            return "image"
    
    return "unknown"