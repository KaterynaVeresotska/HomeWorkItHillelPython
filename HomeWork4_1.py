# Завдання 1 "Написати програму, яка переміщає всі нулі у кінець списку."

my_list = [2, 4, 5, 7, 0, 4, 0, 4, 3, 0, 5]
index = 0
zero_count = 0
length_my_list = len(my_list)
while index < length_my_list - zero_count:
    if my_list[index] == 0:
        my_list.pop(index)
        my_list.append(0)
        zero_count += 1
    else:
        index += 1

print(my_list)
