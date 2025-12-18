"""
QUESTION:
Implement the `optimal_page_replacement` function to simulate the optimal page replacement algorithm. The function should take in two parameters: `pages`, a list of page requests, and `memory_size`, the number of available memory slots. It should return the total number of page faults that occurred. The optimal page replacement algorithm always replaces the page that will not be used for the longest time in the future when a page fault occurs. Assume that the `pages` list is 1-indexed and contains unique page identifiers.
"""

def optimal_page_replacement(pages, memory_size):
    memory_state = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory_state:
            if len(memory_state) < memory_size:
                memory_state.append(pages[i])
            else:
                farthest_page_index = 0
                for j in range(memory_size):
                    if memory_state[j] not in pages[i+1:]:
                        memory_state[j] = pages[i]
                        break
                    else:
                        farthest_page_index = max(farthest_page_index, pages[i+1:].index(memory_state[j]))
                else:
                    memory_state[pages[i+1:].index(memory_state[farthest_page_index])] = pages[i]
            page_faults += 1

    return page_faults