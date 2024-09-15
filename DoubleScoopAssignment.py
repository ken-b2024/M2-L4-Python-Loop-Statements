#Task 1
import random
moods = ['sad', 'happy', 'tired', 'anxious', 'excited']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_times = ['morning', 'afternoon', 'evening']

for weekday in weekdays:
    for times in day_times:
        current_mood = random.choice(moods)
        print("On " + weekday + " in the " + times + " I felt " + current_mood)