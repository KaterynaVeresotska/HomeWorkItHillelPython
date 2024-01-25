# Завдання 2

my_list = [0, 1, 7, 2, 4, 8]
if len(my_list) == 0:
    result = 0
else:
    total_result = 0
    for index in range(0, len(my_list), 2):
        total_result += my_list[index]
    result = total_result * my_list[-1]
print(result)
