"""
QUESTION:
You are given a list of valid seat codes, each representing a unique seat on a plane. Write a function `get_my_seat(seat_codes)` that takes this list as input and returns the seat ID of the missing seat. The missing seat ID is the only one that is not present in the list of seat IDs, but its neighbors (IDs +1 and -1) are present in the list. Assume the input list `seat_codes` is non-empty and contains valid seat codes.
"""

def get_my_seat(seat_codes):
    def get_seat_id(seat_code):
        row = int(seat_code[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(seat_code[7:].replace('L', '0').replace('R', '1'), 2)
        return row * 8 + column

    seat_ids = sorted([get_seat_id(code) for code in seat_codes])
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i-1] == 2:
            return seat_ids[i] - 1
    return None  # No missing seat found