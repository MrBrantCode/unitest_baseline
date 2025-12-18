"""
QUESTION:
Given a list of maturities in days (e.g., 15, 35, 58, 65, 70, 74, 95) and corresponding DV01 values for each maturity, implement a function called `bucket_dv01` to assign each maturity to a fixed maturity bucket (e.g., 1m, 2m, 3m) and calculate the total DV01 for each bucket, assuming the buckets represent the following day ranges: 1m = 0-30 days, 2m = 31-60 days, 3m = 61-90 days. The function should return a dictionary with the bucket names as keys and the total DV01 for each bucket as values.
"""

def bucket_dv01(maturities, dv01_values):
    """
    Assign each maturity to a fixed maturity bucket (1m, 2m, 3m) and calculate the total DV01 for each bucket.

    Args:
    maturities (list): A list of maturities in days.
    dv01_values (list): A list of corresponding DV01 values for each maturity.

    Returns:
    dict: A dictionary with the bucket names as keys and the total DV01 for each bucket as values.
    """

    # Define the bucket ranges in days
    bucket_ranges = {
        "1m": (0, 30),
        "2m": (31, 60),
        "3m": (61, 90)
    }

    # Initialize a dictionary to store the total DV01 for each bucket
    bucket_dv01_values = {bucket: 0 for bucket in bucket_ranges}

    # Iterate over the maturities and DV01 values
    for maturity, dv01 in zip(maturities, dv01_values):
        # Find the corresponding bucket for the maturity
        for bucket, (start, end) in bucket_ranges.items():
            if start <= maturity <= end:
                # Add the DV01 value to the corresponding bucket
                bucket_dv01_values[bucket] += dv01

    return bucket_dv01_values