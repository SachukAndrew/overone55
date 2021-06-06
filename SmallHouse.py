from House import House
if __name__ == '__main__':
    def __str__(self):
        return f"{self.__price}, {self.__area}"
    class SmallHouse(House):
        def __init__(self, price):
            self.__price = price
            self.__area = 40

        def info(self):
            return f"{self.__price}, {self.__area}"
if __name__ == '__main__':
    sml1 = SmallHouse(50000)
#print(sml1.self._price)
#print(sml1.info_House())
    print(sml1.info())


