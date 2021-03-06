"""создание родительского класса"""


class Cars():
    # инициализация атрибутов класса
    def __init__(self, model, year, made, distance):
        self.model = model
        self.year = year
        self.made = made
        self.distance = distance

    # создаем метод выводящий три атрибута класса
    def print_info(self):
        print(self.model, self.year + 'г', self.made)

    # создаем метод выводящий один атрибут класса
    def print_distance(self):
        print('пробег:', (str(self.distance)) + 'км')


"""создание дочернего класса"""


class Electro(Cars):
    # наследование атрибутов родительского класса и присвоение нового
    def __init__(self, model, year, made, distance, battery):
        # присваеваем старые атрибуты к клаасу наследника
        super().__init__(model, year, made, distance)
        # присваеваем классу новый атрибут
        self.battery = battery

    # создаем метод выводящий четыри атрибута класса
    def electro_info(self):
        print(self.model, self.year + 'г', self.made, 'акк:' + self.battery)

    # вывыодим расчеты, исполльзуя новый атрибут класса - battery
    def battery_consumption(self):
        cond = int(self.distance) / 100 * 25
        print('аккамулятор выдал всего:', str(cond), 'вт/ч')


# создаем первый экземпляр
car1 = Cars('BMW', '2004', 'Germany', '200000')
# используем экземпляр в первом методе родительского класса
car1.print_info()
# используем экземпляр во втором методе родительского класса
car1.print_distance()

# создаем второй экземпляр
car2 = Electro('Tesla', '2020', 'USA', '50000', 'Panasonic')
# используем экземпляр в первом методе дочернего класса
car2.electro_info()
# используем экземпляр во втором методе дочернего класса
car2.battery_consumption()
