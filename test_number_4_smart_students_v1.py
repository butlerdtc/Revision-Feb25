# Lists to store results that fit into each list's categories
score_list = []
smart_list = []

while True:
    score = input("Enter a score, or type 'done' to exit: ")
    if score == "done" or score == "Done" or score == "DONE":
        break
    else:
        # Checks if input is a number
        if score.isdigit():
            # Converts the string to an integer
            score_check = int(score)
            if 100 >= score_check >= 0:
                # Adds string to list if it is within valid range
                score_list.append(score)
                continue
            else:
                print("Please enter a value between 0 and 100")
                continue
        else:
            print("Please enter a value between 0 and 100")
            continue

for value in score_list:
    # Converts each string in the list into an integer
    value_int = int(value)
    if value_int >= 80:
        # If integer is greater than (or equal to) 80 adds to high score list
        smart_list.append(value_int)

# Finds number of values in the smart student list
number_smart_students = len(smart_list)
if number_smart_students > 1:
    print(f"\nThis class has {number_smart_students} smart students!")
elif number_smart_students == 1:
    print(f"\nThis class has {number_smart_students} smart student!")
else:
    print("\nThis class has no smart students!")
