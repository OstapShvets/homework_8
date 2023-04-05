# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.


# my_list = ['ostap', 'shv', 'hello', 'hillel',]
# new_list = []
#
# for i in range(len(my_list)):
#     fin = my_list[i]
#     if i % 2 == 0:
#         new_list.append(fin)
#     else:
#         new_list.append(fin[::-1])
# print(new_list)


#######Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list у яких перший символ - буква "a".
#
# my_list = ['ars',
#            'salmon',
#            'africa',
#            'auto',
# ]
# new_list = []
#
# for i in my_list:
#     if i[0] == 'a':
#         new_list.append(i)
# print(new_list)


#Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# my_list = ['ars',
#            'salmon',
#            'bro',
#            'africa',
#            'auto',
# ]
# new_list = []
#
# for i in my_list:
#     if 'a' in i:
#         new_list.append(i)
# print(new_list)


#Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
#а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.


# people = [{"name": "Kristina", "age": 22},
#         {"name": "Andriy", "age": 19},
#            {"name": "Ostap", "age": 18},
#            {"name": "Sophia", "age": 16},
#            {"name": "Oleg", "age": 18},
# ]
# youngest_age = float('inf')
# youngest_names = []
#
# for person in people:
#     if person['age'] < youngest_age:
#         youngest_age = person['age']
#         youngest_names = [person['name']]
#     elif person['age'] == youngest_age:
#         youngest_names.append(person['name'])
#
# print(youngest_names)


# Б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# longest_length = 0
# longest_names = []


# #список вище :)
# longest_length = 0
# longest_names = []
#
# for person in people:
#     if len(person['name']) > longest_length:
#         longest_length = len(person['name'])
#         longest_names = [person['name']]
#     elif len(person['name']) == longest_length:
#         longest_names.append(person['name'])
#
# print(longest_names)


##  B)  Порахувати середню вік усіх людей із початкового списку.

# age = 0
# for person in people:
#     age += person['age']
#
# average_age = age / len(people)
#
# print(average_age)



#############5) Дано два словники my_dict_1 і my_dict_2. а) Створити список із ключів, які є в обох словниках.

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
#
# my_keys = []
# for key in my_dict_1.keys():
#     if key in my_dict_2.keys():
#         my_keys.append(key)
#
# print(my_keys)


###Б)     Створити список із ключів, які є у першому, але немає у другому словнику.


# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
#
# unique_keys = list(my_dict_1.keys() - my_dict_2.keys())
# print(unique_keys)

###B)  Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
#
# new_dict = {}
# for key, value in my_dict_1.items():
#     if key not in my_dict_2.keys():
#         new_dict[key] = value
#
# print(new_dict)


##### Г)Об'єднати ці два словники у новий словник за правилом:якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
#якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
#
# new_dict = my_dict_1.copy()
# for key, value in my_dict_2.items():
#     if key in new_dict.keys():
#         new_dict[key] = [new_dict[key], value]
#     else:
#         new_dict.setdefault(key, value)
#
# print(new_dict)