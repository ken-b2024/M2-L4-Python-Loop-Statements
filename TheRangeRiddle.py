#Task 1
import random
moods = ["happy", "sad", "excited", "anxious"]
weekdays = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']

for weekday in weekdays:
    current_mood = random.choice(moods)
    print("On " + str(weekday) + " I felt " + current_mood)