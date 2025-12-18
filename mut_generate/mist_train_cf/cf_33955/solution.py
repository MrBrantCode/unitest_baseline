"""
QUESTION:
Implement a function `process_data_representations` that takes a list of dictionaries representing data representations. Each dictionary contains the keys "Source" (string), "Point2" (list of three floats), and "Resolution" (integer). The function should return a dictionary containing the total number of data representations, the average resolution of all data representations, and the data source with the highest X coordinate in the "Point2" list.
"""

def process_data_representations(data_representations):
    total_data_representations = len(data_representations)
    total_resolution = sum(rep["Resolution"] for rep in data_representations)
    average_resolution = total_resolution / total_data_representations

    highest_x_source = max(data_representations, key=lambda rep: rep["Point2"][0])["Source"]

    return {
        "total_data_representations": total_data_representations,
        "average_resolution": average_resolution,
        "highest_x_source": highest_x_source
    }