"""
QUESTION:
Implement a function `filter_apps` that takes a list of application names as input and returns a new list containing only the application names present in `APP_STR`. The function should correctly filter the input list based on the elements in `APP_STR`.

The function has access to the predefined list `APP_STR`.
"""

def filter_apps(app_names):
    APP_STR = ['INS', 'VG', 'VG_AHRS', 'Compass', 'Leveler', 'IMU', 'OpenIMU']
    return [app for app in app_names if app in APP_STR]