from typing import List
from pydantic import BaseModel
from task1 import Book, BOOKS_DATABASE


class Library(BaseModel):
    books: List[Book] = []

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        :return: Если книг в библиотеке нет, то вернуть 1, в противном случае вернуть идентификатор последней книги увеличенный на 1.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param book_id: индентификатор книги, которую надо найти
        :return: Если книга существует, то вернуть индекс из списка, в противном случае вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
        """
        for id_x, id_ in enumerate(self.books):
            if book_id == self.books[id_x].id:
                return id_x
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(2))  # проверяем индекс книги с id = 1
