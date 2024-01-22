# Завдання 2 "Перемістити елемент у списку"

my_numbers_list = [3, 4, 5, 6, 2, 5, 6, 6, 9]
if len(my_numbers_list) > 1:
        last_element = my_numbers_list.pop()  #видаляємо останній елемент
        my_numbers_list.insert(0, last_element) #додаємо його на початок
print(my_numbers_list) #[9, 3, 4, 5, 6, 2, 5, 6, 6]


my_numbers_list = [1]
if len(my_numbers_list) > 1:
        last_element = my_numbers_list.pop() #видаляємо останній елемент
        my_numbers_list.insert(0, last_element) #додаємо його на початок
print(my_numbers_list) #[1] список з одним елементом залишиться незмінним.



my_numbers_list = []
if len(my_numbers_list) > 1:
        last_element = my_numbers_list.pop()  # видаляємо останній елемент
        my_numbers_list.insert(0, last_element) #додаємо його на початок
print(my_numbers_list)  #[] Порожній список залишиться незмінним.


my_numbers_list = [5, 88, 8, 9, 3, 5, 7, 8, 9, 2]
if len(my_numbers_list) > 1:
        last_element = my_numbers_list.pop()  # видаляємо останній елемент
        my_numbers_list.insert(0, last_element) #додаємо його на початок
print(my_numbers_list) #[2, 5, 88, 8, 9, 3, 5, 7, 8, 9]