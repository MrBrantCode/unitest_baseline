"""
QUESTION:
Create a function process_sensor_readings that takes 5 arguments: da0, da1, ad0, ad1, and ad2. The function should return a string in the format "da0 = <processed_da0>, da1 = <processed_da1>, ad0 = <processed_ad0>, ad1 = <processed_ad1>, ad2 = <processed_ad2>". The digital readings (da0 and da1) should remain unchanged, while the analog readings (ad0, ad1, and ad2) should be adjusted by the formula int(x * (3.326 - 3.245) / 3.3), where x is the raw analog reading.
"""

def process_sensor_readings(da0, da1, ad0, ad1, ad2):
    processed_da0 = da0
    processed_da1 = da1

    processed_ad0 = int(ad0 * (3.326 - 3.245) / 3.3)
    processed_ad1 = int(ad1 * (3.326 - 3.245) / 3.3)
    processed_ad2 = int(ad2 * (3.326 - 3.245) / 3.3)

    return f"da0 = {processed_da0}, da1 = {processed_da1}, ad0 = {processed_ad0}, ad1 = {processed_ad1}, ad2 = {processed_ad2}"