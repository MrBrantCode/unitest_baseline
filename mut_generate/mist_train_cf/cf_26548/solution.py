"""
QUESTION:
Create a function named `parse_ceph_data` that takes a dictionary `ceph_data` as input. The function should parse the Ceph insights data and return a structured format containing the following information: 
- Cluster name
- Overall health status
- Number of monitors in quorum
- List of monitor names and their health status
- Total number of OSDs
- Number of OSDs in up state
- Number of OSDs in down state 

The input dictionary is expected to be in the following JSON format:
```json
{
  "cluster_name": "my_cluster",
  "health": {
    "overall_status": "HEALTH_OK",
    "detail": "HEALTH_OK"
  },
  "monitors": {
    "total": 3,
    "in_quorum": 3,
    "details": [
      {
        "name": "mon1",
        "health": "HEALTH_OK"
      },
      {
        "name": "mon2",
        "health": "HEALTH_OK"
      },
      {
        "name": "mon3",
        "health": "HEALTH_OK"
      }
    ]
  },
  "osds": {
    "total": 6,
    "in_up": 6,
    "in_down": 0
  }
}
```
"""

def parse_ceph_data(ceph_data: dict) -> dict:
    parsed_data = {
        "cluster_name": ceph_data.get("cluster_name"),
        "overall_health_status": ceph_data["health"]["overall_status"],
        "monitors_in_quorum": ceph_data["monitors"]["in_quorum"],
        "monitor_details": [
            {"name": monitor["name"], "health": monitor["health"]} for monitor in ceph_data["monitors"]["details"]
        ],
        "total_osds": ceph_data["osds"]["total"],
        "osds_in_up_state": ceph_data["osds"]["in_up"],
        "osds_in_down_state": ceph_data["osds"]["in_down"]
    }
    return parsed_data