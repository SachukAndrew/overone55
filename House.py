class House:
    def __str__(self):
        return f"{self.__price}, {self.__area}"
    def __init__(self, price, area):
        self.__area = area
        self.__price = price

    def sell_house(self):
        return self.__price

    def final_price(self, discount):
        if (type(discount) is int or type(discount) is float) and discount < 35:
            self.__price = self.__price*(100 - discount)/100
            return self.__price
        else:
            raise ValueError('Unreal type of discount or the amount of discount moe then 35%')

    def info_House(self):
        return f"{self.__price}, {self.__area}"

if __name__ == '__main__':
    hs1 = House(73000, 82)
    print(hs1.info_House())
    print(hs1.final_price(5))

