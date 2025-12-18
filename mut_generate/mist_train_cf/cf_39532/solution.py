"""
QUESTION:
Implement the `_make_hash_value` method in the `TokenGenerator` class. This method should take two parameters: `appointment` and `timestamp`. It should return a hash value created by concatenating the volunteer's name (`appointment.volunteer`), the appointment's primary key (`appointment.pk`), and the timestamp, all converted to a text type.
"""

def make_hash_value(appointment, timestamp):
    from six import text_type
    return text_type(appointment.volunteer) + text_type(appointment.pk) + text_type(timestamp)