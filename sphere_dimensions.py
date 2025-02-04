import math
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

while True:
      radius = float_checker("Enter the radius of the sphere")
      if radius is not None:
            break
      else:
            continue

pi_value = math.pi
area = 4 * pi_value * (radius ** 2)
volume = (4 / 3) * pi_value * (radius ** 3)
easygui.msgbox(f"Your sphere has a volume of {volume:.2f}cm^3 and an area"
               f" of {area:.2f}cm^2", "Results")
