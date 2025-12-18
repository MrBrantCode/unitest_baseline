"""
QUESTION:
Create a function `detect_overlapping_dates` that takes a list of dates as input, where each date is a tuple of six integers representing the start and end year, month, and day of a date range. The function should return a list of all dates that overlap with at least one other date in the input list.
"""

def detect_overlapping_dates(dates_list):
  overlaps = set()

  for i in range(len(dates_list)-1):
    for j in range(i+1, len(dates_list)):
      date1_start_year, date1_start_month, date1_start_day, date1_end_year, date1_end_month, date1_end_day = dates_list[i]
      date2_start_year, date2_start_month, date2_start_day, date2_end_year, date2_end_month, date2_end_day = dates_list[j]
      if (date1_start_year <= date2_end_year and date2_start_year <= date1_end_year) and (date1_start_month <= date2_end_month and date2_start_month <= date1_end_month) and (date1_start_day <= date2_end_day and date2_start_day <= date1_end_day):
        overlaps.add(dates_list[i])
        overlaps.add(dates_list[j])
  
  return list(overlaps)