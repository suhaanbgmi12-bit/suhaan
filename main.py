steps = []
exercise = []
water = []

with open("fitness_data.txt", "w") as file:
    for i in range(7):
        print("\nDay", i + 1)

        s = int(input("Enter daily steps: "))
        e = int(input("Enter exercise duration in minutes: "))
        w = float(input("Enter water intake in litres: "))

        steps.append(s)
        exercise.append(e)
        water.append(w)

        file.write("Day " + str(i + 1) + "\n")
        file.write("Steps: " + str(s) + "\n")
        file.write("Exercise: " + str(e) + " minutes\n")
        file.write("Water: " + str(w) + " litres\n\n")

step_goal = int(input("\nEnter your daily step goal: "))
exercise_goal = int(input("Enter your daily exercise goal: "))
water_goal = float(input("Enter your daily water goal: "))

with open("fitness_data.txt", "a") as file:
    file.write("\n----- GOALS -----\n")
    file.write("Step goal: " + str(step_goal) + "\n")
    file.write("Exercise goal: " + str(exercise_goal) + "\n")
    file.write("Water goal: " + str(water_goal) + "\n")

avg_steps = sum(steps) / 7
avg_exercise = sum(exercise) / 7
avg_water = sum(water) / 7

step_days = 0
exercise_days = 0
water_days = 0

for i in range(7):
    if steps[i] >= step_goal:
        step_days += 1

    if exercise[i] >= exercise_goal:
        exercise_days += 1

    if water[i] >= water_goal:
        water_days += 1

print("\n----- WEEKLY FITNESS REPORT -----")

print("Average daily steps:", avg_steps)
print("Average exercise time:", avg_exercise, "minutes")
print("Average water intake:", avg_water, "litres")

print("\n----- GOAL COMPLETION -----")

print("Step goal completed:", step_days, "out of 7 days")
print("Exercise goal completed:", exercise_days, "out of 7 days")
print("Water goal completed:", water_days, "out of 7 days")

print("\n----- PROGRESS SUMMARY -----")

if step_days >= 5:
    print("Great job! You are doing well with your steps.")
else:
    print("Try to walk more every day.")

if exercise_days >= 5:
    print("Good work! Your exercise routine is consistent.")
else:
    print("Try to exercise more regularly.")

if water_days >= 5:
    print("Great! You are maintaining good water intake.")
else:
    print("Try to drink more water daily.")

with open("fitness_data.txt", "a") as file:
    file.write("\n----- WEEKLY REPORT -----\n")
    file.write("Average steps: " + str(avg_steps) + "\n")
    file.write("Average exercise: " + str(avg_exercise) + "\n")
    file.write("Average water: " + str(avg_water) + "\n")
    file.write("Step goal completed: " + str(step_days) + "/7 days\n")
    file.write("Exercise goal completed: " + str(exercise_days) + "/7 days\n")
    file.write("Water goal completed: " + str(water_days) + "/7 days\n")

print("\nData saved successfully in fitness_data.txt")
