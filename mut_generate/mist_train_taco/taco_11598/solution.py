"""
QUESTION:
You are standing on top of an amazing Himalayan mountain. The view is absolutely breathtaking! you want to take a picture on your phone, but... your memory is full again! ok, time to sort through your shuffled photos and make some space...

Given a gallery of photos, write a function to sort through your pictures.
You get a random hard disk drive full of pics, you must return an array with the 5 most recent ones PLUS the next one (same year and number following the one of the last).

You will always get at least a photo and all pics will be in the format `YYYY.imgN`

Examples:
```python
sort_photos["2016.img1","2016.img2","2015.img3","2016.img4","2013.img5"]) ==["2013.img5","2015.img3","2016.img1","2016.img2","2016.img4","2016.img5"]
sort_photos["2016.img1"]) ==["2016.img1","2016.img2"]
```
"""

def get_recent_photos_and_next(photos):
    # Split the photo names into year and number
    parsed_photos = [tuple(int(part) for part in photo.split('.img')) for photo in photos]
    
    # Sort the photos by year and then by number
    sorted_photos = sorted(parsed_photos)
    
    # Get the 5 most recent photos
    recent_photos = sorted_photos[-5:]
    
    # Get the last photo in the sorted list
    last_photo = sorted_photos[-1]
    
    # Determine the next photo in the sequence
    next_photo = (last_photo[0], last_photo[1] + 1)
    
    # Combine the recent photos and the next photo
    result = recent_photos + [next_photo]
    
    # Format the result back to the original string format
    formatted_result = [f'{year}.img{number}' for year, number in result]
    
    return formatted_result