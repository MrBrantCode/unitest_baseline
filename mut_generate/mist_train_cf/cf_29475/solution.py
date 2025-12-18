"""
QUESTION:
Given a hotel with n rooms numbered from 1 to n and a list of bookings where each booking is a tuple (i, j, k) representing the starting room number, ending room number, and the number of rooms booked, write a function `generate_occupancy_status(n, bookings)` that returns a list of dictionaries where each dictionary represents the occupancy status of each room. The keys of the dictionary are the room numbers, and the values are the total number of bookings for that room. The function should handle 1 <= n <= 100 and 1 <= i <= j <= n, 1 <= k <= 10^5.
"""

def generate_occupancy_status(n, bookings):
    result = [{} for _ in range(n)]

    for booking in bookings:
        i, j, k = booking[0], booking[1], booking[2]
        for room in range(i, j + 1):
            if room in result[room - 1]:
                result[room - 1][room] += k
            else:
                result[room - 1][room] = k

    return result