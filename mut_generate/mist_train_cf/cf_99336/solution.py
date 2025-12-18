"""
QUESTION:
Create a function `create_workout_plan` that takes in the following parameters: 
- `exercises`: a list of dictionaries containing exercise data (name, difficulty, target muscles)
- `client_name`: the name of the client
- `fitness_level`: the fitness level of the client
- `past_injuries`: a list of past injuries of the client
- `preferred_exercises`: a list of preferred exercises of the client
- `target_muscles`: a list of target muscle groups of the client

The function should return a string representing the workout plan for the client. The workout plan should include exercises that match the client's fitness level, do not target their past injuries, and are related to their target muscle groups. The workout plan should be displayed in the following format:
```
Workout Plan for [Client Name]
Fitness Level: [Fitness Level]
Target Muscles: [Target Muscles]
Exercises:
- [Exercise Name]
```
Note that the function should be able to handle any number of exercises and client data.
"""

def create_workout_plan(exercises, client_name, fitness_level, past_injuries, preferred_exercises, target_muscles):
    """
    Creates a workout plan for a client based on their fitness level, past injuries, 
    preferred exercises, and target muscle groups.

    Args:
    exercises (list): A list of dictionaries containing exercise data (name, difficulty, target muscles)
    client_name (str): The name of the client
    fitness_level (str): The fitness level of the client
    past_injuries (list): A list of past injuries of the client
    preferred_exercises (list): A list of preferred exercises of the client
    target_muscles (list): A list of target muscle groups of the client

    Returns:
    str: A string representing the workout plan for the client
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