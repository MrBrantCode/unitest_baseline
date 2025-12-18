"""
QUESTION:
Implement a Python function called "extract_location_info" that takes a dictionary representing a location's properties as input and returns a new dictionary containing the extracted information. The input dictionary contains various fields including a nested "ExtraData" field with "Address" and "Hours of operations". The function should extract the reference number, name, full address, city, state, postcode, latitude, longitude, phone number, and parsed hours of operation. The function should also implement the parsing of the hours of operation from the "ExtraData" field.
"""

def extract_location_info(row):
    properties = {
        "ref": row["LocationNumber"],
        "name": row["Name"],
        "addr_full": row["ExtraData"]["Address"]["AddressNonStruct_Line1"],
        "city": row["ExtraData"]["Address"]["Locality"],
        "state": row["ExtraData"]["Address"]["Region"],
        "postcode": row["ExtraData"]["Address"]["PostalCode"],
        "lat": row["Location"]["coordinates"][1],
        "lon": row["Location"]["coordinates"][0],
        "phone": row["ExtraData"]["Phone"],
    }

    def parse_hours(hours_str):
        parsed_hours = {}
        days_hours = hours_str.split(", ")
        for day_hour in days_hours:
            day, time = day_hour.split(": ")
            parsed_hours[day] = time
        return parsed_hours

    properties["hours"] = parse_hours(row["ExtraData"]["Hours of operations"])
    return properties