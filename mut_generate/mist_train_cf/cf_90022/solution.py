"""
QUESTION:
Create a function named `calculate_webpage_statistics` that takes a nested dictionary as input where each key represents a webpage and its corresponding value is another dictionary containing the webpage's URL, title, number of images, number of hyperlinks, number of paragraphs, number of headings, and a list of word counts for each paragraph. The function should calculate and return the webpage with the highest number of images and the webpage with the highest average word count per paragraph. 

The input dictionary should be in the following format:

```python
webpages = {
    "webpage1": {
        "url": "https://www.example1.com",
        "title": "Webpage 1",
        "images": 5,
        "hyperlinks": 10,
        "paragraphs": 3,
        "headings": 2,
        "paragraph_word_count": [50, 75, 100]
    },
    # Add details for other webpages...
}
```
"""

def calculate_webpage_statistics(webpages):
    max_images = 0
    max_images_webpage = ""
    max_avg_word_count = 0
    max_avg_word_count_webpage = ""

    for webpage, details in webpages.items():
        if details["images"] > max_images:
            max_images = details["images"]
            max_images_webpage = webpage

        total_word_count = 0
        for paragraph in details["paragraph_word_count"]:
            total_word_count += paragraph
        avg_word_count = total_word_count / len(details["paragraph_word_count"])

        if avg_word_count > max_avg_word_count:
            max_avg_word_count = avg_word_count
            max_avg_word_count_webpage = webpage

    return {
        "max_images_webpage": max_images_webpage,
        "max_avg_word_count_webpage": max_avg_word_count_webpage
    }