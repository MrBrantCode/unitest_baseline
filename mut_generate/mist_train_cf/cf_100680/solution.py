"""
QUESTION:
Implement a function `search_table_of_contents` that searches the table of contents of a weight-loss guide and returns a bullet list of sections that contain the search term. The table of contents is a nested dictionary with main sections and subsections. The search should be case-insensitive and limited to the main sections "Diet", "Exercise", and "Weight-loss tips for beginners". The function should return sections that contain the search term "simple" or "beginner-friendly", and the output should be a bullet list with a hierarchical structure.
"""

def search_table_of_contents(search_term: str, table_of_contents) -> str:
    bullet_list = ""
    for main_section in table_of_contents:
        if main_section in ["Diet", "Exercise", "Weight-loss tips for beginners"]:
            bullet_list += f"\n• {main_section}"
            for subsection in table_of_contents[main_section]:
                if search_term.lower() in subsection.lower():
                    bullet_list += f"\n\t◦ {subsection}"
                elif search_term.lower() == "simple" and "simple" in subsection.lower():
                    bullet_list += f"\n\t◦ {subsection}"
                elif search_term.lower() == "beginner-friendly" and "beginner-friendly" in subsection.lower():
                    bullet_list += f"\n\t◦ {subsection}"
    return bullet_list