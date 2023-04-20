# m =['eryhrtghdfgh', 'wergrth' , 'etyhrthvbthydfgb']
# n = len(m)

# for i in range(0, n):
#     l = len(m[i])
#     if l > 10:
#         a = m[i][0] + str(l-2) + m[i][l-1]
#         print(a)
#     else:
#         print(m[i])


# n = 5

# a = [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1] ,[1, 0, 0]

# count = 0
# for i in range(0, n):
#     if a[i][0] + a[i][1] + a[i][2] > 1:
#         count += 1

# print(count)



# import os
#
# sites = []
# site_names = []
#
# count = int(input('Сколько хотите добавить сайтов: '))
#
# for i in range(1, count+1):
#     sites.append('www.'+input('Введите домен, '+str(i)+'-ого сайта (например: youtube.com): '))
#     site_names.append(input('Введите название '+str(i)+'-ого сайта: '))
#
# print('Список сайтов:')
#
# count = 0
#
# for i in site_names:
#     count += 1
#     print(count, '-', i)
#
# print('\nчтобы завершить работу нажмите enter\n')
#
# while True:
#     site_number = input('Введите номер нужного сайта: ')
#     if site_number == '':
#         break
#     trigger = 0
#     site_number = int(site_number)
#     for i in range(1, count+1):
#         if site_number == i:
#             trigger = 1
#     if trigger == 0:
#         print('Ошибка: некорректный номер сайта!')
#     else:
#         os.system('start ' + sites[site_number - 1])
# print('Пока ;3')



# class Calkulator:
#     def __init__(self, a, b):
#         self.number1 = a
#         self.number2 = b
#     def slojenie(self):
#         return (self.number1 + self.number2)
#     def vichitanie(self):
#         return (self.number1 - self.number2)
#     def umnojenie(self):
#         return (self.number1 * self.number2)
#     def delenie(self):
#         return (self.number1 / self.number2)
#
# calkulation = calkulator(int(input()), int(input()))
# print(calkulation.delenie())




# class Helper:
#     def intput():
#         return int(input('Введите будущее число: '))
#     def listput():
#         return list(input('Введите будущий список: '))
#     def tupput():
#         return tuple(input('Введите будущий кортеж: '))
#
# intput = Helper.intput()
# print(intput)
# listput = Helper.listput()
# print(listput)
# tupput = Helper.tupput()
# print(tupput)

# class human:
#     age = 0
#     name = 'none'
#     surname = 'none'
#     gender = 'none'
#     condition = True
#     height = 0
#     weight = 0
#     def __init__(self, new_name, new_surname, new_gender):
#         self.name = new_name
#         self.surname = new_surname
#         self.gender = new_gender
#     def change_age(self, years):
#         self.age += years
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_surname(self, new_surname):
#         self.surname = new_surname
#     def change_gender(self, new_gender):
#         self.gender = new_gender
#     def change_condition(self, new_codition):
#         self.condition = new_codition
#     def change_weignt(self, new_weight):
#         self.weight = new_weight
#     def change_height(self,new_height):
#         self.height = new_height

import os
import pickle
import time

ludi = []

class humanisation:
    name = 'human'
    surname = 'humanus'
    age = 0
    height = 0
    weight = 0
    def __init__(self, new_name, new_surname):
        self.name = new_name
        self.surname = new_surname
    def change_name(self, new_name):
        self.name = new_name
    def change_surname(self, new_surname):
        self.surname = new_surname
    def change_age(self, new_age):
        self.age = new_age
    def change_height(self, new_height):
        self.height = new_height
    def change_weight(self, new_weight):
        self.weight = new_weight


while True:
    print('Список действий:\n'
          '1) добавить\n'
          '2) изменить\n'
          '3) удалить\n'
          '4) сохранить в файл\n'
          '5) загрузить из файла')
    print('\nчтобы выйти нажмите enter\n')
    request = input('\nвведите номер нужного действия: ')
    if request == '':
        break
    request = int(request)
    if request == 1:
        human = humanisation(input('\nвведите имя нового человека: '), input('введите фамилию нового человека: '))
        ludi.append(human)
        print('\nчеловек', ludi[len(ludi)-1].name, ludi[len(ludi)-1].surname, 'добавлен\n')
        time.sleep(1.5)

    if request == 2:
        print('\nсписок людей: ')
        for i in range(1, len(ludi)+1):
            print(i, '-', ludi[i-1].name, ludi[i-1].surname)
        chose_human = input('\nВведите номер человека которого хотите изменить: ')
        if chose_human == '':
            continue
        chose_human = int(chose_human)-1
        while True:
            print('\nсписок характеристик:\n'
                  '1) имя: ', ludi[chose_human].name, '\n'
                  '2) фамилия: ', ludi[chose_human].surname, '\n'
                  '3) возраст: ', ludi[chose_human].age, '\n'
                  '4) рост: ', ludi[chose_human].height, '\n'
                  '5) вес: ', ludi[chose_human].weight, '\n')
            print('чтобы вернуться нажмите enter\n')
            chose_change = input('что вы хотите изменить: ')
            if chose_change == '':
                break
            chose_change = int(chose_change)
            if chose_change == 1:
                ludi[chose_human].change_name(input('введите новое имя человека: '))
            if chose_change == 2:
                ludi[chose_human].change_age(input('введите новую фамилию человека: '))
            if chose_change == 3:
                ludi[chose_human].change_age(input('введите новый возраст человека: '))
            if chose_change == 4:
                ludi[chose_human].change_height(input('введите новый рост человека: '))
            if chose_change == 5:
                ludi[chose_human].change_weight(input('введите новый вес человека: '))
            print('\nпараметр изменён')
            time.sleep(1.5)
    if request == 3:
        while True:
            print('\nсписок людей: ')
            for i in range(1, len(ludi) + 1):
                print(i, '-', ludi[i - 1].name, ludi[i - 1].surname)
            print('\nчтобы вернуться нажмите enter')
            del_request = input('\nвведите номер человека которого надо удалить: ')
            if del_request == '':
                break
            del_request = int(del_request)
            del(ludi[del_request-1])
            print('\nчеловек удалён')
            time.sleep(1.5)
    if request == 4:
        f = open('123\\saved_ludi.txt', "wb")
        pickle.dump(ludi, f)
        f.close()
        print('\nлюди помещены в файл\n')
        time.sleep(1.5)
    if request == 5:
        f = open('123\\saved_ludi.txt', "rb")
        ludi = pickle.load(f)
        f.close()
        print('\nлюди выгружены\n')
        time.sleep(1.5)


print('\n\n         пока ;3\n')