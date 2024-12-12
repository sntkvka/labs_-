# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class House:
    def __init__(self, room_quantity: float, floor_quantity: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param room_quantity: Количество комнат
        :param floor_quantity: Количество этажей

        Примеры:
        >>> house = House(5.5, 4) # нициализация экземпляра класса
        """
        if not isinstance(room_quantity, (int, float)):
            raise TypeError("Количество комнат должно быть типа int или float")
        if room_quantity < 0:
            raise ValueError("Количество комнат должно быть положительным числом")
        self.room_quantity = room_quantity

        if not isinstance(floor_quantity, (int, float)):
            raise TypeError("Количество этажей должно быть типа int или float")
        if floor_quantity < 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        self.floor_quantity = floor_quantity

    def add_floors(self, floor: int) -> None:
        """
        Постройка дополнительных этажей в доме
        :param floor: Количество добавляемых этажей

        :raise ValueError: Если количество этажей отрицательное число или дробь, вызываем ошибку

        Примеры:
        >>> floors = House(8, 3)
        >>> floors.add_floors (2)
        """
        if not isinstance(floor, (int, float)):
            raise TypeError
        if floor < 0:
            raise ValueError
        ...

    def remove_floors(self, demolish_floor: int) -> None:
        """
        Снесение этажей в доме
        :param demolish_floor: Количество сносимых этажей
        :raise ValueError: Если количество этажей - отрицательное число или дробь, вызываем ошибку

        :return: Количество снесённых этажей

        Примеры:
        >>> floors = House(8, 4)
        >>> floors.remove_floors (4)
        """
        if not isinstance(demolish_floor, (int, float)):
            raise TypeError
        if demolish_floor < 0:
            raise ValueError
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass


class Wildberries:
    def __init__(self, items_amount: int, available_funds: float):
        """
        Создание и подготовка к работе объекта "Вайлдберрис"

        :param items_amount: Количество единиц товара в корзине
        :param available_funds: Количество доступных средств

        Примеры:
        >>> wb = Wildberries(47, 23004.51)  # инициализация экземпляра класса
        """
        if not isinstance(items_amount, int):
            raise TypeError("The number of items in the cart must be of type int")
        if items_amount < 0:
            raise ValueError("The number of items in the cart must be a positive number")
        self.items_amount = items_amount

        if not isinstance(available_funds, (int, float)):
            raise TypeError("Pay attention to the type of value: it must has int or float type!")
        if available_funds < 0:
            raise ValueError("The number of available funds cannot be negative")
        self.available_funds = available_funds

    def is_available_funds(self) -> bool:
        """
        Функция проверяет наличие доступных средств на счету
         :return: Есть ли средства на счету

         Пример:
         >>> available_money = Wildberries(47, 0)
         >>> available_money.is_available_funds
        """
        ...

    def added_sum(self, general_sum: float) -> None:
        """
        Количество денег, положенных на счёт
        :param general_sum: Сумма, которую положили на счёт

        Примеры:
        >>> money = Wildberries(12, 344.15)
        >>> money.added_sum(10000)
        """
        if not isinstance(general_sum, (int, float)):
            raise TypeError("Добавляемая сумма должна быть типа int или float")
        if general_sum < 0:
            raise ValueError("Добавляемая сумма должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass


class Chemistry:
    def __init__(self, components_amount: int, molecular_mass: float):
        """
        Создание и подготовка к работе объекта "Химия"

        :param components_amount: Количество компонентов в полимере
        :param molecular_mass: Молекулярная масса полимера

        Примеры:
        >>> formula = Chemistry(5, 242.7)  # инициализация экземпляра класса
        """
        if not isinstance(components_amount, int):
            raise TypeError
        if components_amount < 0:
            raise ValueError
        self.components_amount = components_amount

        if not isinstance(molecular_mass, (int, float)):
            raise TypeError
        if molecular_mass < 0:
            raise ValueError
        self.molecular_mass = molecular_mass

    def add_compaund(self, new_components: int) -> None:
        """
        Метод описывает добавление новвых мономеров в полимер
        :param new_components: Количество добавляемых мономеров

        Примеры:
        >>> formula = Chemistry(7, 455)
        >>> formula.add_compaund(3)
        """
        if not isinstance(new_components, int):
            raise TypeError
        if new_components < 0:
            raise ValueError
        ...

    def remove_component(self, estimate_molecular_mass: float) -> None:
        """
        Метод описывает молекулярную массу, потерянную при извлечении мономеров.
        :param estimate_molecular_mass: Молекулярная масса извлеченного(-ых) мономера(-ов)
        :raise ValueError: Молекуларная масса извлеченного(-ых) мономера(-ов) не может превышать общую молекулярную
        массу полимера, в противном случае возвращается ошибка.
        :return: Молекулярная масса извлеченного(-ых) мономера(-ов)
        Пример:
        >>> formula = Chemistry(2, 117)
        >>> formula.remove_component(54.7)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
