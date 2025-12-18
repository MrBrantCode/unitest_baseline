"""
QUESTION:
Write a function `corpFlightBookings(bookings, cancellations, n)` that takes as input two arrays of flight bookings and cancellations, where each booking or cancellation is represented as a list of three integers `[first, last, seats]`, and an integer `n` representing the total number of flights. The function should return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i` after considering the cancellations.

Constraints:
- `1 <= n <= 2 * 10^4`
- `1 <= bookings.length, cancellations.length <= 2 * 10^4`
- `bookings[i].length == 3, cancellations[j].length == 3`
- `1 <= firsti, firstj <= lasti, lastj <= n`
- `1 <= seatsi, seatsj <= 10^4`
- For any cancellation, the number of seats cancelled will not exceed the total number of seats booked for that flight.
"""

def corpFlightBookings(bookings, cancellations, n):
    flights = [0] * (n + 1)
    for first, last, seats in bookings:
        flights[first-1] += seats
        if last < n:
            flights[last] -= seats
    for first, last, seats in cancellations:
        flights[first-1] -= seats
        if last < n:
            flights[last] += seats
    for i in range(1, n):
        flights[i] += flights[i-1]
    return flights[:-1]