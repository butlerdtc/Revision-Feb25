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


sound = 0.340
while True:
    time = float_checker("How many seconds were there between the lightning and "
                         "thunder?")
    if time is not None:
        break
    else:
        continue
distance = sound * time
easygui.msgbox(f"The storm is {distance:.2f} kilometres away")
