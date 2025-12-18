"""
QUESTION:
Create a function named `process_vehicle_status` that takes a list of vehicle documents and an action as input, and returns the updated list of vehicle documents. Each vehicle document is a dictionary with keys "vehicle_id", "vehicle_status", and "reference_doc_name". The function should update the "vehicle_status" and "reference_doc_name" based on the action. If the action is "reserve", set "vehicle_status" to "Reserved" and "reference_doc_name" to a given reference document name. If the action is "cancel", set "vehicle_status" to "Available" and clear "reference_doc_name".
"""

from typing import List, Dict

def process_vehicle_status(vehicle_docs: List[Dict[str, str]], action: str, reference_doc_name: str) -> List[Dict[str, str]]:
    for vehicle_doc in vehicle_docs:
        if action == "reserve":
            vehicle_doc["vehicle_status"] = "Reserved"
            vehicle_doc["reference_doc_name"] = reference_doc_name
        elif action == "cancel":
            vehicle_doc["vehicle_status"] = "Available"
            vehicle_doc["reference_doc_name"] = ""
    return vehicle_docs