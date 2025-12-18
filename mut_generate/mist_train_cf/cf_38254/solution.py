"""
QUESTION:
Write a function named `calculate_total_resources` that calculates the total number of resources needed for a system given the following parameters: 
- `number_of_rows`: The total number of rows of Index Servers.
- `number_of_links`: The number of links to be sent to the Crawler.
- `number_of_chunks`: The number of chunks to be sent to the Index Builder.
- `number_of_comps`: The number of components managed by each Watchdog.

Each component requires the following resources: 
- Each Index Server: 100 units
- Crawler: 50 units per link
- Index Builder: 200 units per chunk
- Watchdog: 20 units per component managed.

Return the total number of resources needed, which is the sum of resources required for Index Servers, Crawler, Index Builder, and Watchdog.
"""

def calculate_total_resources(number_of_rows, number_of_links, number_of_chunks, number_of_comps):
    resources_per_index_server = 100
    resources_per_link = 50
    resources_per_chunk = 200
    resources_per_comp = 20

    total_resources_index_servers = number_of_rows * resources_per_index_server
    total_resources_crawler = number_of_links * resources_per_link
    total_resources_index_builder = number_of_chunks * resources_per_chunk
    total_resources_watchdog = number_of_comps * resources_per_comp

    total_resources_needed = (total_resources_index_servers +
                              total_resources_crawler +
                              total_resources_index_builder +
                              total_resources_watchdog)

    return total_resources_needed