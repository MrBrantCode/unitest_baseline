"""
QUESTION:
Implement a function `snowflakeToUnix` that takes a 64-bit Snowflake ID as input and returns the corresponding Unix timestamp in seconds. The function should apply the following formula: (1) right shift the Snowflake ID by 22 bits to extract the timestamp part, (2) add 1420070400000 to the extracted timestamp, and (3) divide the result by 1000 to convert the timestamp from milliseconds to seconds. The function signature is `def snowflakeToUnix(snowflake: int) -> int:`.
"""

def snowflakeToUnix(snowflake: int) -> int:
    return ((snowflake >> 22) + 1420070400000) // 1000