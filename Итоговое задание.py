if __name__ == "__main__":
    # Write your solution here
    class Vehicle:
        mileage = 0

        def __init__(self, car_brand: str, engine_power: int, color: str, oil_consumption: float):
            """
            Создание и подготовка к работе родительского объекта Vehicle
            :param car_brand: марка автомобиля
            :param engine_power: мощность двигателя
            :param color: цвет
            :param oil_consumption: расход топлива
            Примеры:
            >>> tachka = Vehicle("Audi", 444, "черный", 41.5)
            >>> tachka.car_brand()
            """
            self.car_brand = car_brand
            self.engine_power = engine_power
            self.color = color
            self.oil_consumption = oil_consumption

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(car_brand = {self.car_brand!r}, engine_power ={self.engine_power!r}, color={self.color!r}, oil_consumption={self.oil_consumption})"

        def __str__(self) -> str:
            return f"Автомобиль марки {self.car_brand!r} с мощностью двиагателя равной: {self.engine_power} л.с. и {self.color} цветом"

        def oil(self, distance: float) -> float:
            """
            Метод, который считает потраченное автомобилем топливо
            :return: возвращет F-строку
            Пример:
            >>>Tachila = Vehicle("Toyota", 155, "черный", 9.42)
            >>>Tachila.oil(150)
            """
            get_consumption = self.oil_consumption / 100 * distance
            self.mileage += distance
            return f"Автомобиль марки: {self.car_brand!r} потратит за {distance}км. дороги {get_consumption} литров топлива"

        def get_miliage(self):
            return f"Автомобиль суммарно проехал {self.mileage}"


    class PassengerCar(Vehicle):

        def __init__(self, car_brand: str, engine_power: int, color: str, oil_consumption: float, number_of_seats: int):
            super().__init__(car_brand, engine_power, color, oil_consumption)
            self.number_of_seats = number_of_seats

            """
            Создание и подготовка к работе родительского объекта PassengerCar

            Наследуем следующие атрибуты из родительского класса Vehicle:

            :param car_brand: марка автомобиля
            :param engine_power: мощность двигателя
            :param color: цвет
            :param oil_consumption: расход топлива

            :param number_of_seats: количество мест

            Примеры:
            >>>tachka1 = PassengerCar("Audi", 250, "черный", 21.5, 4)
            >>>tachka1.car_brand()
            """

        def __str__(self) -> str:
            return f"Легковой автомобиль марки {self.car_brand!r} с мощностью двиагателя равной: {self.engine_power} л.с., c {self.color} цветом и количество сидячих мест равным {self.number_of_seats}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, engine_power={self.engine_power}, color={self.color!r}, number_of_seats={self.number_of_seats}, oil_consumption={self.oil_consumption})"


    class Truck(Vehicle):
        """
            Создание и подготовка к работе родительского объекта Truck
            Унаследуем следующие атрибуты из родительского класса Vehicle:
            :param car_brand: марка автомобиля
            :param engine_power: мощность двигателя
            :param color: цвет
            :param oil_consumption: расход топлива
            :param load_capacity: грузоподъемность автомобиля
            Примеры:
            >>>tachka1 = PassengerCar("Audi", 444, "черный", 41.5, 30)
            >>>tachka1.car_brand()
            """

        def __init__(self, car_brand: str, engine_power: int, color: str, oil_consumption: float, load_capacity: int):
            super().__init__(car_brand, engine_power, color, oil_consumption)
            self.load_capacity = load_capacity

        def __str__(self) -> str:
            return f"Грузовой автомобиль марки {self.car_brand!r} с мощностью двиагателя равной: {self.engine_power} л.с., c  {self.color} цветом и грузоподъёмностью равной {self.load_capacity}т."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, engine_power={self.engine_power}, color={self.color!r}, number_of_seats={self.load_capacity}, oil_consumption={self.oil_consumption})"

        def oil(self, distance: float, have_trailer: bool) -> float:
            """
            Метод, перегружен из родительского класса. Поскольку наличие прицепа увеличивает потребеление на 30%
            :return: возвращет F-строку
            Пример:
            >>>Tachila = Truck("Volvo", 155, "черный", 9.42)
            >>>Tachila.oil(150, True)
            """

            if have_trailer:
                get_consumption = (self.oil_consumption / 100 * distance) * 1.3
            else:
                get_consumption = (self.oil_consumption / 100 * distance)
            self.mileage += distance

            return f"Автомобиль марки: {self.car_brand!r} потратит за {distance}км. дороги {get_consumption} литров топлива"

auto1 = PassengerCar("Toyota", 155, "черный", 9.42, 5)
print(auto1.oil(150))
print(auto1.oil(200))
print(auto1.get_miliage())
auto2 = Truck("Volvo", 500, "красно-сииний", 45.3, 30)
print(auto2.oil_consumption)
print(auto2.oil(55, True))
print(auto2.oil(55, False))
print(auto2.get_miliage())
