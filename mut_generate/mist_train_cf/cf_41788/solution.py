"""
QUESTION:
Create a function `process_photos` that takes a list of photo dictionaries as input, where each dictionary contains the keys "id", "count", and "url", and returns a dictionary with the following information: the total number of photos processed, the photo with the highest view count, the photo with the lowest view count, and the average view count of all the photos. The input list can be empty or contain one or more dictionaries, and the function should handle these cases accordingly.
"""

def process_photos(photos: list) -> dict:
    if not photos:
        return {
            "total_photos": 0,
            "photo_highest_views": None,
            "photo_lowest_views": None,
            "average_views": 0
        }

    total_photos = len(photos)
    view_counts = [photo["count"] for photo in photos]
    highest_views_photo = max(photos, key=lambda x: x["count"])
    lowest_views_photo = min(photos, key=lambda x: x["count"])
    average_views = sum(view_counts) / total_photos

    return {
        "total_photos": total_photos,
        "photo_highest_views": highest_views_photo,
        "photo_lowest_views": lowest_views_photo,
        "average_views": average_views
    }