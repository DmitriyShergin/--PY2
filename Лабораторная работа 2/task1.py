from pydantic import BaseModel


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    id: int
    name: str
    pages: int

    def __str__(self) -> str:
        """
        Метод __str__, возвращающий строку формата, где "название_книги" берется с помощью атрибута name

        :return: Строка 'Книга (название_книги)'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод __repr__, возвращающий валидную python строку, по которой можно инициализировать точно такой же экземпляр

        :return:
        """
        return f'{self.__class__.__name__}(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__