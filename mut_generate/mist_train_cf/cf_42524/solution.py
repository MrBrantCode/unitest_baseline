"""
QUESTION:
Implement the `update_booking_data` function to update a data structure with customer information and group booked rooms by their type ID. 

The function should take in two parameters: 
- `customer`: An object containing customer information with the following attributes: `country`, `email`, `first_name`, and `last_name`. 
- `booking`: An object containing booking information with the following attributes: `booked_rooms`, a list of objects representing the booked rooms, where each object has the attribute `room_type_id`.

The function should append the customer information to the 'Customers' list under the 'Booking' key in the data structure and group the booked rooms by their type ID in a dictionary where the keys are the room type IDs and the values are lists of booked rooms of that type.
"""

def update_booking_data(customer, booking):
    """
    Updates a data structure with customer information and groups booked rooms by their type ID.

    Args:
    - customer (object): An object containing customer information.
    - booking (object): An object containing booking information.

    Returns:
    - data (dict): A dictionary containing the updated customer information.
    - room_groups (dict): A dictionary of booked rooms grouped by their type ID.
    """

    data = {'Booking': {'Customers': []}}
    data['Booking']['Customers'].append({
        'CustomerCountry': customer.country,
        'CustomerEmail': customer.email,
        'CustomerFName': customer.first_name,
        'CustomerLName': customer.last_name
    })

    room_groups = {}
    for booked_room in booking.booked_rooms:
        if booked_room.room_type_id not in room_groups:
            room_groups[booked_room.room_type_id] = []
        room_groups[booked_room.room_type_id].append(booked_room)

    return data, room_groups