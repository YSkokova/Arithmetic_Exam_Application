import random
lists_1 = [2, 3, 4, 5, 6, 7, 8, 9]
lists_2 = ['+', '-', '*']
a = random.choice(lists_1)
b = random.choice(lists_2)
c = random.choice(lists_1)
print(a,b,c)
user_input = int(input())
addition = 0
subtraction = 0
multiplication = 0

if b == "+":
    addition = int(a) + int(c)
elif b == "-":
    subtraction = int(a) - int(c)
elif b == '*':
    multiplication = int(a) * int(c)

if user_input == addition:
    print("Right!")
elif user_input == subtraction:
    print("Right!")
elif user_input == multiplication:
    print("Right!")
else:
    print("Wrong!")
