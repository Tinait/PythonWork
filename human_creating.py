class Human:
    age = 0
    name = 'none'
    surname = 'none'
    gender = 'none'
    condition = 'none'
    height = 0
    weight = 0
    def __init__(self, new_name, new_surname, new_gender):
        self.name = new_name
        self.surname = new_surname
        self.gender = new_gender
        self.condition = 'здоров'
        self.height = 27
        self.weight = 2
    def old_up(self, years):
        self.age += years
        if self.age <= 18:
            self.height = int(27 + self.age * 8.5)
            self.weight = int(2 + self.age * 3.5)
        else:
            self.height = 180
            self.weight = 65
        if self.age >= 80:
            self.condition = 'умер'
        print('\nчеловек -', self.name, self.surname, '\n'
              'состояние -', self.condition, '\n'
              'характеристики: \n'
              ' * лет -', self.age, '\n'
              ' * рост -', self.height, 'см\n'
              ' * вес -', self.weight, 'кг\n'
              ' * пол -', self.gender, '\n')
print('\nВведите имя, фамилию и пол нового человека: ')
humanius = Human(input('имя - '), input('фамилия - '), input('пол - '))

print('\nчеловек -', humanius.name, humanius.surname, '\n'
              'состояние -', humanius.condition, '\n'
              'характеристики: \n'
              ' *', humanius.age, 'лет\n'
              ' * рост -', humanius.height, 'см\n'
              ' * вес -', humanius.weight, 'кг\n'
              ' * пол -', humanius.gender, '\n')

print('попробуйте добавить возраст своему человеку.\n'
      'вы всегда можете выйти, просто нажмите enter\n')

while True:
    request = int(input('насколько '+str(humanius.name)+' должен повзрослеть? - '))
    if request == '':
        break
    if humanius.age + request > 80:
        humanius.old_up(80 - humanius.age)
        break
    humanius.old_up(request)

print('\n\n         пока ;3\n')