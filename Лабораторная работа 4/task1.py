from typing import Union
import doctest


class Car:
    def __init__(self, model: str, engine_capacity: Union[int, float], mileage: Union[int, float]):
        """
        Создание и подготовка к работе базового класса Car

        :param model: модель автомобиля (тип str)
        :param engine_capacity: объем двигателя (тип float или int)
        :param mileage: пробег (тип float или int)
        Пример:
        >>> car = Car("Camry", 3.5, -1)
        Traceback (most recent call last):
            ...
        ValueError: Пробег автомобиля должен быть положительным числом или равен 0
        """
        self.model = model
        self.engine_capacity = engine_capacity
        self.mileage = mileage

    def __str__(self) -> str:
        """
        Магический метод __str__, который выводит информацию о классе в виде для пользователя
        :return: строка "Машина марки <название модели> c объемом двигателя <объем двигателя> и
        пробегом <пробег автомобиля>
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(car1)
        Машина марки Camry с объемом двигателя 3.5 и пробегом 322.
        """
        return f"Машина марки {self._model} с объемом двигателя {self._engine_capacity} и пробегом {self._mileage}."

    def __repr__(self) -> str:
        """
        Магические метод repr, который выводит информацию о классе в виде для программиста

        :return: строка "<Название класса>(model=<название модели>,
        engine capacity=<объем двигателя>, mileage=<пробег>)"
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(repr(car1))
        Car(model=Camry, engine capacity=3.5, mileage=322)
        """
        return f"{self.__class__.__name__}(model={self._model}, engine capacity={self._engine_capacity}, " \
               f"mileage={self._mileage})"

    @property
    def model(self) -> str:
        """
        Гэттер для названия модели автомобиля

        :return: модель автомобиля (это protected атрибут, тип str)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(car1.model)
        Camry
        """
        return self._model  # атрибут _model это protected атрибут, чтобы можно было вызывать сеттер и геттер в __init__

    @model.setter
    def model(self, new_model: str):
        """
        Сэттер для названия модели автомобиля

        :param new_model: новое название модели, которое присваивается (тип str)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> car1.model = 10
        Traceback (most recent call last):
            ...
        TypeError: Наименование модели должно быть типа: str
        """
        if not isinstance(new_model, str):
            raise TypeError("Наименование модели должно быть типа: str")
        self._model = new_model

    @property
    def engine_capacity(self) -> Union[int, float]:
        """
        Геттер для объема двигателя

        :return: объем двигателя (защищенный атрибут типа: int или float)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(car1.engine_capacity)
        3.5
        """
        return self._engine_capacity    # атрибут защищенный, чтобы можно было вызывать геттер и сеттер

    @engine_capacity.setter
    def engine_capacity(self, new_capacity: float):
        """
        Сеттер для объема двигателя

        :param new_capacity: значение объема двигателя, которое присваивается атрибуту (тип int или float)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> car1.engine_capacity = 10
        >>> print(car1.engine_capacity)
        10
        """
        if not isinstance(new_capacity, Union[int, float]):
            raise TypeError("Объем двигателя должен быть типа: int или float")
        if new_capacity <= 0:
            raise ValueError("Объем двигателя должен быть положительным числом")
        self._engine_capacity = new_capacity

    @property
    def mileage(self) -> Union[int, float]:
        """
        Геттер для пробега автомобиля

        :return: пробег автомобиля (защищенный атрибут типа int или float)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(car1.mileage)
        322
        """
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage: Union[int, float]):
        """
        Сеттер для пробега автомобиля

        :param new_mileage: значение нового пробега (тип int или float)
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> car1.mileage = 1000
        >>> print(car1.mileage)
        1000
        """
        if not isinstance(new_mileage, Union[int, float]):
            raise TypeError("Пробег автомобиля должен быть типа: int или float")
        if new_mileage < 0:
            raise ValueError("Пробег автомобиля должен быть положительным числом или равен 0")
        self._mileage = new_mileage

    def create_dict(self) -> dict:
        """
        Метод, объединяющий всю информацию о машине в словарь
        :return: словарь, содерщажий информацию о машине
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> print(car1.create_dict())
        {'Модель': 'Camry', 'Объем двигателя': 3.5, 'Пробег': 322}
        """
        return {"Модель": self._model, "Объем двигателя": self._engine_capacity, "Пробег": self._mileage}

    def zero_mileage(self):
        """
        Метод обнуляющий пробег автомобиля, данный метод наследуется в классе CargoCar, так как
        Пример:
        >>> car1 = Car("Camry", 3.5, 322)
        >>> car1.zero_mileage()
        >>> print(car1.mileage)
        0
        """
        self._mileage = 0


class CargoCar(Car):
    def __init__(self, model: str, engine_capacity: Union[int, float],
                 mileage: Union[int, float], trailer_capacity: Union[int, float]):
        """
        Создание и подготовка к работе дочернего класса CargoCar, наследуется от базового класса Car

        :param model: значение атрибута, который отвечает за название модели, наследуется от класса Car
        :param engine_capacity: значение атрибута, который отвечает за объем двигателя, наследуется от класса Car
        :param mileage: значение атрибута, который отвечает за пробег, наследуется от класса Car
        :param trailer_capacity: атрибут отвечающи за объем прицепа (тип int или float, данный атрибут в сеттере
        задается приватным, так как такой атрибут свойственен только грузовому транспорту, а данный класс не является
        базовым для другого)
        Пример:
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> print(car)
        Машина марки KAMAZ с объемом двигателя 9.5 и пробегом 1337. Объем прицепа: 560.0
        """
        super().__init__(model, engine_capacity, mileage)
        self.trailer_capacity = trailer_capacity

    def __str__(self) -> str:
        """
        Магический метод str перегружается, так как появился новый атрибут
        :return: строка в виде, удобном для пользователя
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> str(car)
        'Машина марки KAMAZ с объемом двигателя 9.5 и пробегом 1337. Объем прицепа: 560.0'
        """
        return super(CargoCar, self).__str__() + f" Объем прицепа: {self.__trailer_capacity}"

    def __repr__(self) -> str:
        """
        Магический метод repr перегружается, так как появился новый атрибут
        :return: строка в виде удобном для программиста
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> print(repr(car))
        CargoCar(model=KAMAZ, engine capacity=9.5, mileage=1337, trailer capacity=560.0)
        """
        return f"{self.__class__.__name__}(model={self._model}, engine capacity={self._engine_capacity}, " \
               f"mileage={self._mileage}, trailer capacity={self.__trailer_capacity})"

    @property
    def trailer_capacity(self) -> Union[int, float]:
        """
        Геттер для атрибута, отвечающего за объем прицепа

        :return:объем прицепа (тип данный int или float)
        Пример:
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> car.trailer_capacity
        560.0
        """
        return self.__trailer_capacity

    @trailer_capacity.setter
    def trailer_capacity(self, new_capacity: Union[int, float]):
        """
        Сеттер для объема кузова

        :param new_capacity: новое значение объема кузова (тип int или float)
        Пример:
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> car.trailer_capacity = -10
        Traceback (most recent call last):
            ...
        ValueError: Объем прицепа должен быть положительным числом
        """
        if not isinstance(new_capacity, Union[int, float]):
            raise TypeError("Объем прицепа должен быть типа: int или float")
        if new_capacity <= 0:
            raise ValueError("Объем прицепа должен быть положительным числом")
        self.__trailer_capacity = new_capacity

    def create_dict(self) -> dict:
        """
        Метод создающий словарь состоящий из информации об автомобиле. Он перегружается из класса Car, так как
        добавляется новая пара ключ-значение

        :return: словарь с новой парой ключ-значение
        Пример:
        >>> car = CargoCar("KAMAZ", 9.5, 1337, 560.0)
        >>> car.create_dict()
        {'Модель': 'KAMAZ', 'Объем двигателя': 9.5, 'Пробег': 1337, 'Объем прицепа': 560.0}
        """
        cargo_dict = super(CargoCar, self).create_dict()
        cargo_dict["Объем прицепа"] = self.__trailer_capacity
        return cargo_dict

    # метод zero_mileage наследуется из базового класса, так как он изменяет наследуемый атрибут и ничего не возвращает


def main():
    car3 = Car("Camry", 3.5, 322)
    print(car3.__dict__, car3.model)
    dict_car = car3.create_dict()
    print(dict_car)
    car3.zero_mileage()
    print(car3.__dict__)
    cargo_car1 = CargoCar("KAMAZ", 9.5, 1337, 560.0)
    print(cargo_car1.create_dict())
    cargo_car1.zero_mileage()
    print(cargo_car1.create_dict())
    print(repr(cargo_car1))


if __name__ == "__main__":
    doctest.testmod()
    main()
