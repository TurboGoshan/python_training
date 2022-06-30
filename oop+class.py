# создаем класс с названием
class Restauran():
    # присваеваем классу два атрибута: restaurant_name, cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # создаем метод использующий атрибуты
    def describe_restaurant(self):
        print("ресторан '" + self.restaurant_name + "' - ", self.cuisine_type + " кухня")

    # создаем метод без атрибутов
    def open_restaurant(self):
        print('вкусно и не дорого!')


# создаем триэкземпляра с данными: restaurant_name, cuisine_type
rest1 = Restauran('Тбилиси', 'кавказская')
rest2 = Restauran('Пильменная', 'русская')
rest3 = Restauran('Палермо', 'итальянская')

# вызываем методы для экземпляров
rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()
rest1.open_restaurant()


class Users():
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(self.first_name, self.last_name, self.email, self.password)

    def greet_user(self):
        print('информация о пользователе:')

user1 = Users('Виктор', 'Попов', 'popov@sd.ru', '12345')
user2 = Users('Иван', 'Самойленко', 'samivan@gmail.com', 'misfits85')

user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()