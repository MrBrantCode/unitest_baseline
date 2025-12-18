"""
QUESTION:
Implement a function `count_router_prefixes` that takes a list of strings representing router prefixes in the format `app.include_router(router, prefix="/vector")` and returns a dictionary where the keys are the router names and the values are the count of unique prefixes associated with each router. The input list is guaranteed to contain valid router prefixes in the specified format.
"""

from typing import List, Dict
import re

def count_router_prefixes(prefix_list: List[str]) -> Dict[str, int]:
    router_prefix_count = {}
    
    for prefix in prefix_list:
        router_name = re.search(r'app\.include_router\((.*?),', prefix).group(1).strip()
        router_prefix = re.search(r'prefix="(.*?)"', prefix).group(1)
        
        if router_name in router_prefix_count:
            router_prefix_count[router_name].add(router_prefix)
        else:
            router_prefix_count[router_name] = {router_prefix}
    
    return {router: len(prefixes) for router, prefixes in router_prefix_count.items()}