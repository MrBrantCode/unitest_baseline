"""
QUESTION:
Implement a function `parse_hlt_monitoring_config(config)` that takes a configuration string as input and returns a dictionary containing the extracted information. The dictionary should have the following keys: "FolderName", "HLTPaths", "JetSelection", "JetId", and "NumJets". The function should parse the configuration string and extract the corresponding values for each key.
"""

import re

def parse_hlt_monitoring_config(config):
    result = {}
    
    folder_match = re.search(r"FolderName\s*=\s*'([^']*)'", config)
    if folder_match:
        result["FolderName"] = folder_match.group(1)
    
    hlt_paths_match = re.search(r"hltPaths\s*=\s*\[([^\]]*)\]", config)
    if hlt_paths_match:
        result["HLTPaths"] = re.findall(r'"(.*?)"', hlt_paths_match.group(1))
    
    jet_selection_match = re.search(r"jetSelection\s*=\s*\"(.*?)\"", config)
    if jet_selection_match:
        result["JetSelection"] = jet_selection_match.group(1)
    
    jet_id_match = re.search(r"jetId\s*=\s*\"(.*?)\"", config)
    if jet_id_match:
        result["JetId"] = jet_id_match.group(1)
    
    num_jets_match = re.search(r"njets\s*=\s*(\d+)", config)
    if num_jets_match:
        result["NumJets"] = int(num_jets_match.group(1))
    
    return result