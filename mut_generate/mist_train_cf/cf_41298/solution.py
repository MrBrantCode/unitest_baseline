"""
QUESTION:
Implement a function `process_traffic_data` that takes in three parameters: `locationdata`, `recognition`, and `data`. The function should iterate through the `links` in `locationdata` to find the link with an `id` matching the `id` in `recognition`. It should then calculate the average speed using the formula `average_speed = (distance / travel time) * 3.6` and extract the hour of the day from the `date` in `data`. The function should output two strings in the format: 
`LongValueSum:<recognition_id>_<hour_of_day>_speedsum\t<average_speed>` and 
`LongValueSum:<recognition_id>_<hour_of_day>_speedcount\t1`. 

Assume that `locationdata` is a dictionary with a `links` key containing a list of dictionaries with `id`, `dist`, and `links` keys, `recognition` is a dictionary with `id` and `tt` keys, and `data` is a dictionary with a `date` key in the format 'YYYY-MM-DDTHH:MM:SS'.
"""

def process_traffic_data(locationdata, recognition, data):
    for item in locationdata['links']:
        if item['id'] == recognition['id']:
            link_data = item
            average_speed = (link_data['dist'] / recognition['tt']) * 3.6
            hour_of_day = data['date'][11:13]

            return (
                f"LongValueSum:{recognition['id']}_{hour_of_day}_speedsum\t{int(average_speed)}",
                f"LongValueSum:{recognition['id']}_{hour_of_day}_speedcount\t1"
            )