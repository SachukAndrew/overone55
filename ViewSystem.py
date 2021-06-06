from System import System
from House import House
from Human import Human


class ViewSystem:
    def __init__(self):
        self.__human = []
        self.__house = []

    def __str__(self):
        return f"{self.__human}, {self.__house}"

    @property
    def human(self):
        return self.__human

    @property
    def house(self):
        return self.__house


    def make_house(self, house, price, area):
        System.make_house(house, price, area)
        self.__house.append(System.make_house(house, price, area))
        return System.make_house(house, price, area)

    def make_human(self, human, name, age, money):
        System.make_human(human, name, age, money)
        self.__human.append(System.make_human(human, name, age, money))
        return System.make_human(human, name, age, money)

    def see_houses(self):
        return self.house

    def see_humans(self):
        return self.__human

    def choose_house(self, house):

        pass

    def choose_human(self):
        pass

    def buy_house(self):
        pass

if __name__ == '__main__':
    VS = ViewSystem()
    #print(VS.make_house('house1', 60000, 60))
    #print(VS.make_human('human1', 'Irina', 36, 20000))
    #VS.make_human('human2', 'VLAS', 35, 20000)
    #print(VS.see_houses())
    #print(VS.see_humans())


    def info():
        print('Добро пожаловать в систему по покупке домов.\n'
              'Для покупки дома нужно ввести свои данные (Имя, возраст, колличество денег),\n'
              'а так же выбрать дом из списка.\n'
              'Для ввода данных контрагента нажмите 1\n'
              'Для просмотра списка контрагентов нажмите 2\n'
              'Для добавления желаемого дома нажмите 3\n'
              'Для просмотра списка домов нажмите 4\n'
              'Для выбора дома нажмите 5\n'
              'Для выбора контрагента нажмите 6\n'
              'Для покупки дома нажмите 7\n'
              'Для выхода из системы нажмите 0')

    def Choise():
        return int(input('Сделайте Ваш выбор от 1 до 6, 0 - выход из системы: '))


    choice = None
    while choice != '0':
        print('Информация Info')
        choice = input('Сделайте ваш выбор: ')
        if choice == '1':

            human = 'human'
            name = input('Введите имя: ')
            age = int(input('введите возраст: '))
            money = int(input('Введите количество денег: '))
            h = VS.make_human(human, name, age, money)

        elif choice == '2':
            print(VS.see_humans())

        elif choice == '3':
            house = 'house'
            price = int(input('Введите стоимость дома: '))
            area = int(input('Введите площадь дома: '))
            hs = VS.make_house(house, price, area)

        elif choice == '4':
            print(VS.make_house())

        elif choice == '0':
            print('Goodby')
    input('Веедите Enter для завершения')

