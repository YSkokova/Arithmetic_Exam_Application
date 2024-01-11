import random

# With the first message, the program should ask for a difficulty level:
# 1 - simple operations with numbers 2-9
# 2 - integral squares 11-29
levels_list = ["simple operations with numbers 2-9",
               "integral squares of 11-29"]
choices = ["yes", "YES", "y", "Yes"]
print("Which level do you want? Enter a number:")
print("1 - simple operations with numbers 2-9")
print("2 - integral squares of 11-29")
ex_choice = 0
user_choice = int(input())
mark = 0
while user_choice != 1 or user_choice != 2:
    #  For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
    if user_choice == 1:
        for _ in range(5):
            operations = [" + ", " - ", " * "]
            question = str(random.randint(2, 9)) + \
                random.choice(operations) + str(random.randint(2, 9))
            print(question)
            while True:
                try:
                    user_input = int(input())
                    if user_input == eval(question):
                        print("Right!")
                        mark += 1
                    else:
                        print("Wrong!")
                    break
                except ValueError:
                    print("Incorrect format.")
                    continue
        break

    # For the second difficulty level: the task is an integer; the answer is the square of this number.
    elif user_choice == 2:
        for _ in range(5):
            question = int(random.randint(11, 29))
            print(question)
            while True:
                try:
                    user_input = int(input())
                    if user_input == question ** 2:
                        print("Right!")
                        mark += 1
                    else:
                        print("Wrong!")
                    break
                except ValueError:
                    print("Incorrect format.")
                    continue
        break
    else:
        print("Incorrect format.")
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        user_choice = int(input())
print("Your mark is {}/5. Would you like to save the result? Enter yes or no.".format(mark))
choice2 = input().strip()
if choice2 in choices:
    name = input("What is your name?\n")
    ex_choice = user_choice - 1
    selected_level = levels_list[ex_choice]
    s = "{}: {}/5 in level {} ({}).".format(name,
                                            mark, user_choice, selected_level)
    with open("results.txt", "a") as f:
        f.write(s)
    print('The results are saved in "results.txt".')
