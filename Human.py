from House import House


class Human:
    default_name = 'Egor'
    default_age = 30

    def __init__(self, money, name=default_name, age=default_age):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__house = []

    def __str__(self):
        return f"{self.__name}, {self.__age}, {self.__money}"

    def info(self):
        return f"{self.__name}, {self.__age}, {self.__money}, {self.__house}"

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house.append(house)
        else:
            print('Too small money to buy house')

    def earn_money(self, add_money):
        if type(add_money) is int or type(add_money) is float:
            self.__money = self.__money + add_money
            return self.__money
        else:
            raise ValueError('Incorrect type of parametr add_money - should be int or float')

    def buy_house(self, house, discount):
        try:
            self.__make_deal(house, discount)
        except:
            raise print('Too small money to by house')

#sh = System.make_human(45000, 'Vasia', 35)
#print(sh.info())
if __name__ == '__main__':
    hs1 = House(73000, 82)
    h1 = Human(100000)
    print(h1.info())
    h1.buy_house(hs1.info_House(), hs1.final_price(5))
    print(h1.info())
    h2 = Human(10000, 'Vasia', 20)
    print(h2.info())

