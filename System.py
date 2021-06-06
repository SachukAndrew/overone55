from House import House
from Human import Human


class System:
    def __init__(self):
        self.__humans = []
        self.__houses = []

    def __str__(self):
        return f"{self.__humans}, {self.__houses}"

    @property
    def humans(self):
        return self.__humans

    @property
    def houses(self):
        return self.__houses

    def info(self):
        return len(self.houses), len(self.humans)

    def add_house(self, house):
        self.__houses.append([house])
        return self.__houses

    def add_human(self, human):
        self.__humans.append([human])
        return self.__humans
    def view_houses(self):
        return self.__houses

    def choose_house(self, house):
        try:
            self.__houses[(self.__houses.index(house))]
        except:
            print('There is no sach house in the list')
        return self.__houses[(self.__houses.index(house))]

    def buy_house(self, house):
        self.__houses.remove(self.choose_house(house))

    def make_human(self, money, name, age):
        if (type(age) is int or type(age) is float) and (type(money) is int or type(money) is float) and 0 < age <150:
            human = Human(money, name, age)
            return System.add_human(self, human)
        else:
            raise ValueError('Unreal age')


    def make_house(house, price, area):
        if (type(price) is int or type(price) is float) and (type(area) is int or type(area) is float):
            house = [price, area]
        else:
            raise ValueError('Unreal type of price or area')
        return house

if __name__ == '__main__':
    sys = System()
    hs2 = House(70000, 80)
    hs3 = House(85000, 90)
    hs4 = sys.make_house(95000, 90)
    sys.add_house(hs2.info_House())
    sys.add_house(hs3.info_House())
    sys.add_house(hs4)
    print(sys.info())
    print(sys.view_houses())
    print(sys.info())
    System.make_human(10000, 'Vasia', 20)









