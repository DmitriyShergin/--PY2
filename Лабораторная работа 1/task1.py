import doctest
from typing import Union


class Client:
    def __init__(self, client_name: str, client_adres: str):
        """
        Создание и подготовка к работе объекта "Клиент"

        :param client_name: Имя клиента
        :param client_adres: Адрес клиента

        Пример:
        >>> client = Client("Дмитрий", "СПб")
        >>> print(client.client_name)
        Дмитрий
        """
        self.client_base = {}

        if not isinstance(client_name, str):
            raise TypeError("Имя клиента должно быть типа str")
        self.client_name = client_name

        if not isinstance(client_adres, str):
            raise TypeError("Адрес клиента должно быть типа str")
        self.client_adres = client_adres

        self.add_elements_dict(client_name, client_adres)

    def add_elements_dict(self, client_name: str, client_adres: str) -> dict[str, str]:
        """
        Функция, которая собирает словарь, где ключ это имя клиента, а значение его адрес

        :param client_name: Имя клиента, которое является ключом в словаре
        :param client_adres: Адрес клиента, который является значением в словаре
        :return: Словарь составленный из имени и адреса

        Пример:
        >>> client1 = Client('Саша', "Москва")
        >>> client1.add_elements_dict('Дима', "СПб")
        {'Саша': 'Москва', 'Дима': 'СПб'}
        """
        self.client_base[client_name] = client_adres
        return self.client_base

    def clear_dict(self) -> None:
        """
        Функция, очищающая словарь

        :return: Пустой словарь

        Пример:
        >>> client1 = Client("Даша", "Архангельск")
        >>> client1.clear_dict()
        >>> print(client1.client_base)
        {}
        """
        return self.client_base.clear()


class Table:
    def __init__(self, material: str, color: str):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал, из которого сделан стол
        :param color: Цвет стола

        Пример:
        >>> table1 = Table("Дерево", "Черный")
        >>> print(table1.material, table1.color)
        Дерево Черный
        """
        self.table_items = []

        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

        if not isinstance(color, str):
            raise TypeError('Цвет стола должен быть типа str')
        self.color = color

    def add_table_items(self, elem: str, separator: str = ' ') -> list[str]:
        """
        Добавление предметов на стол

        :param elem: Предметы, добавляемые на стол
        :param separator: Разделитель, между словами в списке предметов (по умолчанию: пробел)
        :return: Список, состоящий из названий предметов, лежащих на столе

        Пример:
        >>> table1 = Table("Дерево", "Черный")
        >>> table1.add_table_items("Персики листья нож")
        ['Персики', 'листья', 'нож']
        """
        if not isinstance(elem, str):
            raise TypeError("Предметы, добавляемые на стол, должны быть типа str")
        self.table_items = elem.split(separator)
        return self.table_items

    def count_table_items(self) -> int:
        """
        Функция, считающая количество предметов на столе

        :return: Количество элементов на столе

        >>> table1 = Table("Пластиковый", "Синий")
        >>> table1.add_table_items("Стакан тарелка")
        ['Стакан', 'тарелка']
        >>> print(table1.count_table_items())
        2
        """
        return len(self.table_items)


class Car:
    def __init__(self, car_model: str, engine_volume: Union[int, float], car_mileage: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param car_model: Модель автомобиля (тип str)
        :param engine_volume: Объем двигателя (тип int или float)
        :param car_mileage: Пробег автомобил (тип int)

        Примеры:
        >>> car1 = Car('Toyota Camry', 3.5, 100500)
        >>> print(car1.engine_volume)
        3.5
        """
        if not isinstance(car_model, str):
            raise TypeError('Модель машины должна быть типа str')
        self.car_model = car_model

        if not isinstance(engine_volume, (int, float)):
            raise TypeError("Объем двигателя должен быть типа int ли float")
        if engine_volume <= 0:
            raise ValueError("Объем двигателя не может быть отрицательным или равным нулю")
        self.engine_volume = engine_volume

        if not isinstance(car_mileage, int):
            raise TypeError("Пробег машины должен быть типа int")
        if car_mileage < 0:
            raise ValueError("Пробег машины не может быть отрицательным")
        self.car_mileage = car_mileage

    def add_car_mileage(self, mileage: int) -> int:
        """
        Функция прибавляет пробег к существующему

        :param mileage: Пробег автомобиля (тип int)
        :return: Обновленный пробег автомобиля (тип int)

        Пример:
        >>> car1 = Car('Toyota Camry', 3.5, 100500)
        >>> car1.add_car_mileage(10)
        100510
        """
        self.car_mileage += mileage
        return self.car_mileage

    def create_car_base(self) -> dict:
        """
        Функция объединяет всю информацию о машине в словарь

        :return: Словарь содержащий информацию об автомобиле (тип dict)

        Пример:
        >>> car1 = Car('Toyota Camry', 3.5, 100500)
        >>> car1.create_car_base()
        {'Модель автомобиля': 'Toyota Camry', 'Объем двигателя': 3.5, 'Пробег автомобиля': 100500}
        """
        car_inf = {}
        car_inf["Модель автомобиля"] = self.car_model
        car_inf["Объем двигателя"] = self.engine_volume
        car_inf['Пробег автомобиля'] = self.car_mileage
        return car_inf


if __name__ == "__main__":
    doctest.testmod()
    pass
