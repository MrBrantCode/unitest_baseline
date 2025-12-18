"""
QUESTION:
Implement the FAIR (Findable, Accessible, Interoperable, Reusable) principles in a database design for storing geographical data, specifically zebra crossing locations. The database has the following restrictions: the table should include a foreign key 'id_user' referencing a user table, and the data will be accessible via API calls.
"""

def create_zebra_crossing(id_zebra_crossing, latitude, longitude, date_uploaded, description, city, id_user, license_url):
    return {
        "id_zebra_crossing": id_zebra_crossing,
        "latitude": latitude,
        "longitude": longitude,
        "date_uploaded": date_uploaded,
        "description": description,
        "city": city,
        "id_user": id_user,
        "license_url": license_url
    }