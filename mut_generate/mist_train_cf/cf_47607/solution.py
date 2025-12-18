"""
QUESTION:
Implement a function `book_room` that takes in a hotel branch, room type, and customer information, and returns a booking ID if the room is available, otherwise returns an error message. The function should also update the room status in the database and send a confirmation email to the customer. The room selection should be based on various parameters like room size, amenities, and view.
"""

def book_room(hotel_branch, room_type, customer_info):
    """
    Books a hotel room based on the provided parameters.

    Args:
        hotel_branch (str): The branch of the hotel.
        room_type (str): The type of room to book.
        customer_info (dict): A dictionary containing customer information.

    Returns:
        str: A booking ID if the room is available, otherwise an error message.
    """

    # Connect to the database
    # For this example, we will use a mock database
    database = {
        "rooms": [
            {"id": 1, "branch": "New York", "type": "Single", "status": "Available"},
            {"id": 2, "branch": "New York", "type": "Double", "status": "Occupied"},
            {"id": 3, "branch": "Los Angeles", "type": "Single", "status": "Available"},
        ]
    }

    # Filter rooms based on branch and type
    available_rooms = [room for room in database["rooms"] if room["branch"] == hotel_branch and room["type"] == room_type and room["status"] == "Available"]

    # Check if any rooms are available
    if available_rooms:
        # Book the first available room
        booked_room = available_rooms[0]
        booked_room["status"] = "Occupied"

        # Generate a booking ID
        booking_id = booked_room["id"]

        # Send a confirmation email to the customer
        # For this example, we will just print a message
        print(f"Booking confirmed. Booking ID: {booking_id}")

        return booking_id
    else:
        return "Error: No rooms available."