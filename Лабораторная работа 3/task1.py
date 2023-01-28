class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе базового класса Book

        :param name: название книги (тип: str) protected
        :param author: имя автора (тип: str) protected
        """
        self._name = name
        self._author = author

    def __str__(self):
        """
        Метод, возвращающий строку в виде для пользователя

        :return: строка в виде 'Книга <название книги>. Автор <автор книги>'
        """
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """
        Метод, возвращающий строку в виде для программиста

        :return: строка в виде '<название класса>(name=<название книги>, author=<автор книги>)'
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """
        Геттер, который возвращает название книги

        :return: название книги
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Геттер, который возвращает имя автора

        :return: имя автора
        """
        return self._author


class PaperBook(Book):
    """Дочерний класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе дочернего класса PaperBook, основанного на Book

        :param name: название книги, наследуется из класса Book
        :param author: имя автора, наследуется из класса Book
        :param pages: количество страниц (тип: int)
        """
        super().__init__(name, author)
        # if not isinstance(pages, int):
        #     raise TypeError("Количество страниц должно быть типа int")
        # if pages <= 0:
        #     raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        """
        Метод, возвращающий строку в виде для пользователя

        :return: строка в виде 'Бумажная книга <название книги>. Автор <автор книги>. Количество страниц <количество страниц>'
        """
        return f"Бумажная книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        """
        Метод, возвращающий строку в виде для программиста

        :return: строка в виде '<название класса>(name=<название книги>, author=<автор книги>, pages=<количество страниц>)'
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self) -> int:
        """
        Геттер, который возвращает количество странниц

        :return: количество страниц
        """
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        """
        Сеттер, который изменяет количество страниц

        :param pages: новое количество страниц
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages


class AudioBook(Book):
    """Дочерний класс аудиокниги"""
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе дочернего класса AudioBook, основанного на Book

        :param name: название книги, наследуется из Book
        :param author: имя автора, наследуется из Book
        :param duration: длительность книги (тип: float)
        """
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        """
        Метод, возвращающий строку в виде для пользователя

        :return: строка в виде 'Аудиокнига <название книги>. Автор <автор книги>. Длительность <длительность>'
        """
        return f"Аудиокнига {self._name}. Автор {self._author}. Длительность {self._duration}"

    def __repr__(self):
        """
        Метод, возвращающий строку в виде для программиста

        :return: строка в виде '<название класса>(name=<название книги>, author=<автор книги>, duration=<длительность>)'
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        """
        Геттер, который возвращает длительность аудиокниги

        :return: длительность аудиокниги
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        """
        Сеттер, который изменяет длительность аудиокниги

        :param duration: новая длительность аудиокниги
        """
        if not isinstance(duration, float):
            raise TypeError("Длительность книги должна быть типа int")
        if duration <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self._duration = duration
