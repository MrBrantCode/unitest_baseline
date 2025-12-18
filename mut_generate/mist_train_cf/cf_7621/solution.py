"""
QUESTION:
Create a function named `analyze_webpages` that takes a dictionary of webpages as input. Each webpage in the dictionary should have a URL, title, number of images, number of hyperlinks, number of paragraphs, number of headings, and a list of word counts for each paragraph. The function should calculate and return the webpage with the highest number of images and the webpage with the highest average word count per paragraph.

The input dictionary will have the following structure:
```python
webpages = {
    "webpage_name": {
        "url": "webpage_url",
        "title": "webpage_title",
        "images": int,
        "hyperlinks": int,
        "paragraphs": int,
        "headings": int,
        "paragraph_word_count": list
    }
}
```
The function should return a tuple containing the name of the webpage with the highest number of images and the name of the webpage with the highest average word count per paragraph.
"""

def analyze_webpages(webpages):
    """
    This function analyzes a dictionary of webpages and returns the webpage with the highest number of images and 
    the webpage with the highest average word count per paragraph.

    Args:
        webpages (dict): A dictionary of webpages where each webpage has a URL, title, number of images, 
                         number of hyperlinks, number of paragraphs, number of headings, and a list of word counts for each paragraph.

    Returns:
        tuple: A tuple containing the name of the webpage with the highest number of images and the name of the webpage 
               with the highest average word count per paragraph.
    """

    max_images = 0
    max_images_webpage = ""

    max_avg_word_count = 0
    max_avg_word_count_webpage = ""

    for webpage, details in webpages.items():
        # Find the webpage with the highest number of images
        if details["images"] > max_images:
            max_images = details["images"]
            max_images_webpage = webpage

        # Find the webpage with the highest average word count per paragraph
        avg_word_count = sum(details["paragraph_word_count"]) / len(details["paragraph_word_count"])
        if avg_word_count > max_avg_word_count:
            max_avg_word_count = avg_word_count
            max_avg_word_count_webpage = webpage

    return max_images_webpage, max_avg_word_count_webpage