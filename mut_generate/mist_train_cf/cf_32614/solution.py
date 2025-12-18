"""
QUESTION:
Create a function `parse_review_data(html_code)` that takes a string `html_code` as input, representing an HTML-like code snippet of a single review. The function should calculate the average rating, extract the user's display name, company name, review title, and review description, and return a summary report. The report should include the average rating, user's display name, company name, review title, and a truncated review description (limited to 200 characters). The average rating should be calculated based on the number of filled and empty star ratings represented by `<i>` tags with class "icon_star" and "icon_star empty", respectively.
"""

import re

def parse_review_data(html_code):
    # Parse star ratings
    filled_stars = len(re.findall(r'<i class="icon_star"></i>', html_code))
    empty_stars = len(re.findall(r'<i class="icon_star empty"></i>', html_code))
    total_stars = filled_stars + empty_stars
    average_rating = filled_stars / total_stars * 5 if total_stars > 0 else 0

    # Extract user's display name, company name, review title, and review description
    user_match = re.search(r'<strong>(.*?)</strong>', html_code)
    company_match = re.search(r'<a href="(.*?)">(.*?)</a>', html_code)
    title_match = re.search(r'"(.*?)"', html_code)
    description_match = re.search(r'<p>(.*?)</p>', html_code)

    user_display_name = user_match.group(1) if user_match else ""
    company_name = company_match.group(2) if company_match else ""
    review_title = title_match.group(1) if title_match else ""
    review_description = description_match.group(1) if description_match else ""

    # Generate summary report
    summary_report = {
        "Average Rating": f"{average_rating:.2f}/5.00",
        "User": user_display_name,
        "Company": company_name,
        "Review Title": review_title,
        "Review Description": review_description[:200]
    }

    return summary_report