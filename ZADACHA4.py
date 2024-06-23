
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
