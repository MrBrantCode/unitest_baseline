"""
QUESTION:
Implement the `apply_query_filter` method of the `ContentExpiryChangelistQueryFilterSetting` class, which takes a site and a queryset as input and returns the filtered queryset. The queryset should be filtered based on the content expiry settings defined by the `expiry_date` and `is_active` parameters. If the `expiry_date` is in the past or the `is_active` flag is set to `False`, the content should be excluded from the queryset. The function should return a filtered queryset that only includes active content that has not expired.
"""

from datetime import date

def apply_query_filter(site, queryset):
    # Get the current date
    current_date = date.today()
    
    # Apply query filter based on content expiry settings
    filtered_queryset = queryset.filter(
        expiry_date__gte=current_date,  # Exclude expired content
        is_active=True  # Exclude inactive content
    )
    
    return filtered_queryset