"""
QUESTION:
Create a function named `create_workout_plan` that takes in four parameters: `exercises`, `client_name`, `fitness_level`, `past_injuries`, `preferred_exercises`, and `target_muscles`. The function should filter the exercises based on the client's fitness level, past injuries, preferred exercises, and target muscle groups, and then create a workout plan in a specific format. The function should return the workout plan as a string.

The `exercises` parameter is a list of dictionaries, where each dictionary represents an exercise and has the following keys: `name`, `difficulty`, and `target_muscles`. The `client_name`, `fitness_level`, and `past_injuries` parameters are strings. The `preferred_exercises` and `target_muscles` parameters are lists of strings. The workout plan should be in the following format:
```
Workout Plan for [Client Name]
Fitness Level: [Fitness Level]
Target Muscles: [Target Muscles]
Exercises:
- [Exercise Name]
```
"""

def create_workout_plan(exercises, client_name, fitness_level, past_injuries, preferred_exercises, target_muscles):
    """
    Creates a workout plan based on the client's fitness level, past injuries, preferred exercises, and target muscle groups.

    Parameters:
    exercises (list): A list of dictionaries representing exercises with 'name', 'difficulty', and 'target_muscles' keys.
    client_name (str): The client's name.
    fitness_level (str): The client's fitness level.
    past_injuries (list): A list of the client's past injuries.
    preferred_exercises (list): A list of the client's preferred exercises.
    target_muscles (list): A list of the client's target muscle groups.

    Returns:
    str: The workout plan as a string.
    """
    # Filter exercises based on client data
    filtered_exercises = []
    for exercise in exercises:
        if exercise["difficulty"] == fitness_level and \
        not any(injury in exercise["target_muscles"] for injury in past_injuries) and \
        any(muscle in exercise["target_muscles"] for muscle in target_muscles) and \
        exercise["name"] in preferred_exercises:
            filtered_exercises.append(exercise)
    # Create workout plan
    workout_plan = f"Workout Plan for {client_name}\nFitness Level: {fitness_level}\nTarget Muscles: {', '.join(target_muscles)}\nExercises:\n"
    for exercise in filtered_exercises:
        workout_plan += f"- {exercise['name']}\n"
    return workout_plan