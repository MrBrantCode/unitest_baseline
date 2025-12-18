"""
QUESTION:
Write a function `points_to_influx` that takes a dictionary `netstat_data` as input, where `netstat_data` contains nested dictionaries with network statistics, and returns a string in the format `measurement_name,type=measurement_type key1=value1,key2=value2,...`. The input dictionary has the structure `netstat_data = {"statistics": {...}}`, where the inner dictionaries contain various network statistics. The function should iterate through the statistics, extract the key-value pairs, and format them into the required string. The output string should start with "bsd_netstat,type=netstat".
"""

def points_to_influx(netstat_data):
    points_netstat = {}
    for x in netstat_data["statistics"]:
        for k, v in netstat_data["statistics"][x].items():
            points_netstat[k] = v
    field_tags = ",".join(["{k}={v}".format(k=str(x[0]), v=x[1]) for x in list(points_netstat.items())])
    return ("bsd_netstat,type=netstat {}").format(field_tags)