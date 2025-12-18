"""
QUESTION:
Write a function `generate_user_json` that generates a valid JSON object describing the given user information. The JSON object should have a nested structure to represent the user's education, previous job, certifications, and projects. The function should also calculate and include additional key-value pairs for the user's years of experience, total project duration, total number of technologies used, average project duration, most used technology, and project descriptions.
"""

def generate_user_json(user_info):
    """
    Generates a valid JSON object describing the given user information.
    
    Args:
    user_info (dict): A dictionary containing user information.
    
    Returns:
    dict: A dictionary representing the JSON object.
    """
    
    # Initialize the result dictionary with the given user information
    result = {
        "name": user_info["name"],
        "age": user_info["age"],
        "location": user_info["location"],
        "jobTitle": user_info["jobTitle"],
        "company": user_info["company"],
        "salary": user_info["salary"],
        "skills": user_info["skills"],
        "education": user_info["education"],
        "previousJob": user_info["previousJob"],
        "certifications": user_info["certifications"],
        "projects": user_info["projects"]
    }
    
    # Calculate years of experience
    years_of_experience = 2023 - user_info["education"]["graduationYear"]
    result["yearsOfExperience"] = years_of_experience
    
    # Calculate total project duration
    total_project_duration = sum([int(project["duration"].split()[0]) for project in user_info["projects"]])
    result["totalProjectDuration"] = f"{total_project_duration} months"
    
    # Calculate total number of technologies used
    technologies_used = set()
    for project in user_info["projects"]:
        technologies_used.update(project["technologiesUsed"])
    result["totalTechnologiesUsed"] = len(technologies_used)
    
    # Calculate average project duration
    average_project_duration = total_project_duration / len(user_info["projects"])
    result["averageProjectDuration"] = f"{average_project_duration:.1f} months"
    
    # Find most used technology
    technology_usage = {}
    for project in user_info["projects"]:
        for technology in project["technologiesUsed"]:
            technology_usage[technology] = technology_usage.get(technology, 0) + 1
    most_used_technology = max(technology_usage, key=technology_usage.get)
    result["mostUsedTechnology"] = most_used_technology
    
    # Get project descriptions
    project_descriptions = [project["description"] for project in user_info["projects"]]
    result["projectDescriptions"] = project_descriptions
    
    return result