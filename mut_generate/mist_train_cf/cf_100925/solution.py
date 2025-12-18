"""
QUESTION:
Create a function `create_workout_plan` that takes four parameters: `client_name`, `fitness_level`, `past_injuries`, and `target_muscles`. The function should return a string representing a personalized workout plan for the client based on their fitness level, past injuries, and target muscle groups, using the provided exercise data. The workout plan should include exercises that match the client's fitness level, do not target their past injuries, and are related to their target muscle groups. The plan should be in the following format:
```
Workout Plan for [Client Name]
Fitness Level: [Fitness Level]
Target Muscles: [Target Muscles]
Exercises:
- [Exercise Name]
```
"""

def create_workout_plan(client_name, fitness_level, past_injuries, target_muscles):
    exercises = [
        {"name": "Pilates Reformer", "difficulty": "Intermediate", "target_muscles": ["Core", "Legs"]},
        {"name": "Yoga Vinyasa Flow", "difficulty": "Intermediate", "target_muscles": ["Glutes", "Core"]},
        {"name": "HIIT Cardio", "difficulty": "Advanced", "target_muscles": ["Full Body"]}
    ]

    filtered_exercises = []
    for exercise in exercises:
        if exercise["difficulty"] == fitness_level and \
        not any(injury in exercise["target_muscles"] for injury in past_injuries) and \
        any(muscle in exercise["target_muscles"] for muscle in target_muscles):
            filtered_exercises.append(exercise)

    workout_plan = f"Workout Plan for {client_name}\nFitness Level: {fitness_level}\nTarget Muscles: {', '.join(target_muscles)}\nExercises:\n"
    for exercise in filtered_exercises:
        workout_plan += f"- {exercise['name']}\n"

    return workout_plan