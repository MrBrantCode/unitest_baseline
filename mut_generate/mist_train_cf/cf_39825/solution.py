"""
QUESTION:
Create a function `count_os` that takes a list of strings representing operating systems in the format "Operating System :: Vendor :: Version" and returns a dictionary containing the count of each unique operating system. The dictionary keys should be the unique operating systems (Vendor :: Version) and the values should be the count of each operating system in the input list.
"""

def count_os(os_list):
    os_count = {}
    for os in os_list:
        os_name = os.split(" :: ")[1] + " :: " + os.split(" :: ")[2]
        if os_name in os_count:
            os_count[os_name] += 1
        else:
            os_count[os_name] = 1
    return os_count