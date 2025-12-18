"""
QUESTION:
Create a function `parse_metadata(metadata)` that takes a list of strings representing metadata as input and returns a dictionary containing the extracted information. The metadata list contains strings in the following formats:
- Operating System: "Operating System ::" followed by the name of the operating system
- Topic: "Topic ::" followed by the category of the topic
- Python Requires: "python_requires=" followed by the required Python version

The function should return a dictionary with keys "operating_systems", "topics", and "python_requires", containing lists of operating systems, topics, and the required Python version, respectively.
"""

def parse_metadata(metadata):
    extracted_data = {"operating_systems": [], "topics": [], "python_requires": ""}
    
    for item in metadata:
        if item.startswith("Operating System ::"):
            extracted_data["operating_systems"].append(item.replace("Operating System :: ", ""))
        elif item.startswith("Topic ::"):
            extracted_data["topics"].append(item.replace("Topic :: ", ""))
        elif item.startswith("python_requires="):
            extracted_data["python_requires"] = item.split("=")[1]

    return extracted_data