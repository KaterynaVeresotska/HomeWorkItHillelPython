# Завдання 1 "Найпростіший калькулятор"

number_input_1 = int(input("Ввести число a = "))
number_input_2 = int(input("Ввести число b = "))
operation = input("Ввести дію над цими числами (+, -, *, /): ")

if operation == '+':
    summ = number_input_1 + number_input_2
    print(f"Ваш результат : {summ}")
elif operation == '-':
    minus = number_input_1 - number_input_2
    print(f"Ваш результат : {minus}")
elif operation == '*':
    multiplication = number_input_1 * number_input_2
    print(f"Ваш результат : {multiplication}")
elif operation == '/':
    if number_input_2 != 0:
        division = number_input_1 / number_input_2
        print(f"Ваш результат : {division}")
    else:
        print("Дільник дорівнює 0!")
else:
    print("Невірний знак операції!")
