import easygui

# Function to check if value entered is a float
def float_checker(question):
    while True:
        number = easygui.enterbox(question)
        # Checks if user selected 'cancel' on easygui box
        if number is None:
            return None
        # This checks if the characters are numbers and if there is only one
        # decimal point and if the decimal point is removed that only numbers
        # are left
        if number.isnumeric() or (number.count('.') == 1 and
                                  number.replace('.', '').isnumeric()):
            # Converts number to a rounded float
            float_number = round(float(number), 3)
            return float_number
        else:
            easygui.msgbox("Please enter a number", "Error")


swimming_calories = 275
jogging_calories = 475
cycling_calories = 200

swimming_hours = 0
cycle_hours = 0
jogging_hours = 0

while True:
    menu = easygui.buttonbox("What exercise would you like to record",
                             "Exercises",
                             ["Swimming", "Cycling", "Jogging", "Finished"])
    if menu == "Swimming":
        swim_hours_question = float_checker("How many hours did you swim?")
        if swim_hours_question is not None:
            swimming_hours = swim_hours_question
        else:
            continue
    elif menu == "Cycling":
        cycling_hours_question = float_checker("How many hours did you cycle?")
        if cycling_hours_question is not None:
            cycle_hours = cycling_hours_question
        else:
            continue
    elif menu == "Jogging":
        jogging_hours_question = float_checker("How many hours did you jog?")
        if jogging_hours_question is not None:
            jogging_hours = jogging_hours_question
        else:
            continue
    else:
        break

total_swim_calories = swimming_calories * swimming_hours
total_cycle_calories = cycling_calories * cycle_hours
total_jog_calories = jogging_calories * jogging_hours

total_calories = (total_swim_calories + total_jog_calories +
                  total_cycle_calories)
calories_to_kg = 3500 / 0.454
weight_lost = total_calories / calories_to_kg
easygui.msgbox(f"You lost {weight_lost:.3f}kgs")