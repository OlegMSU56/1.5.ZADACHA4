
class Building:
    def __init__(self, total):
        self.total = total

    def __str__(self):
        return f'Объект №{self.total}'

    def obj_generator(self):
        while self.total < 40:
            self.total += 1
            obj = Building(self.total)
            print(obj)


obj = Building(0)
obj.obj_generator()



'''
class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Имя:{self.name}')
        print(f'Возраст:{self.age}')
        print(f'Деньги:{self.__money}')
        print(f'Дом:{self.__house}')
    @staticmethod
    def default_info():
        print(f'default_Имя:{Human.default_name}')
        print(f'default_Возраст:{Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Заработал {amount}. Всего {self.__money}')

    def buy_house(self, house, discount):
        pass

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

#if __name__ == '__main__':
    #print(Human.default_name)


Ihtior = Human('Ихтиёр', 27)
Ihtior.info()
Ihtior.earn_money(500)
Ihtior.info()
'''