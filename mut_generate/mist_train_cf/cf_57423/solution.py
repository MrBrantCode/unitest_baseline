"""
QUESTION:
Convert a given time in Eastern Daylight Time (EDT) to Japan Standard Time (JST). The input time is a string in 24-hour format. Japan does not observe Daylight Saving Time, but EDT may be either in standard time or daylight time. The function should take into account that EDT may need to be adjusted for Daylight Saving Time, which would require adding either 13 or 14 hours to convert to JST. 

The function `convert_edt_to_jst` should take a string representing a time in EDT and return the corresponding time in JST as a string.
"""

from datetime import datetime, timedelta

def convert_edt_to_jst(edt_string):
    edt_time = datetime.strptime(edt_string, '%H:%M')
    jst_time = edt_time + timedelta(hours=13)
    
    # The %H:%M format directive extracts hour and minute only.
    return jst_time.strftime('%H:%M')