"""
QUESTION:
Create a program that contains information about 10 different webpages. Each webpage should have the following attributes: url, title, number of images, number of hyperlinks, number of paragraphs, number of headings, and average word count per paragraph. The program should be able to find and display the webpage with the highest number of images and the webpage with the highest average word count per paragraph. 

Function name: Not specified, but it can be 'find_webpage_info' or similar.

Restrictions: The program should be able to handle at least 10 webpages and should be able to find the webpage with the highest number of images and the webpage with the highest average word count per paragraph.
"""

def find_webpage_info(webpages):
    """
    Find the webpage with the highest number of images and the webpage with the highest average word count per paragraph.

    Args:
        webpages (dict): A dictionary containing information about different webpages.

    Returns:
        tuple: A tuple containing the title of the webpage with the highest number of images and the title of the webpage with the highest average word count per paragraph.
    """
    # Finding webpage with the highest number of images
    max_images = max(webpages, key=lambda x: webpages[x]['images'])

    # Finding webpage with the highest average word count per paragraph
    max_avg_word_count = max(webpages, key=lambda x: webpages[x]['average_word_count_per_paragraph'])

    return webpages[max_images]['title'], webpages[max_avg_word_count]['title']