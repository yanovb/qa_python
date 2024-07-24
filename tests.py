import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_add_new_book_with_genre(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_genre()['Шерлок Холмс'] == 'Детективы'

    @pytest.mark.parametrize('book', ['Братья Карамазовы', 'Бесы'])
    def test_set_book_genre_add_new_book_with_another_genre_is_empty(self, collector, book):
        collector.add_new_book(book)
        collector.set_book_genre(book, 'Экзистенциальная драма')

        assert collector.get_books_genre()[book] == ''

    def test_get_book_genre_add_new_book_and_genre_get_genre(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_get_books_with_specific_genre_add_book_with_genre(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс']

    def test_get_books_genre_add_two_books(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Братья Карамазовы')

        assert collector.get_books_genre() == {'Шерлок Холмс': 'Детективы', 'Братья Карамазовы': ''}

    def test_get_books_for_children_add_books(self, collector):
        books = {
            'Шерлок Холмс': 'Детективы',
            'Гарри Поттер': 'Фантастика',
            'Сказка о царе салтане': 'Мультфильмы',
            'Зов Ктулуху': 'Ужасы'
        }
        for key in books:
            collector.add_new_book(key)
            collector.set_book_genre(key, books[key])

        for book in collector.get_books_for_children():
            assert book in ['Гарри Поттер', 'Сказка о царе салтане']

    def test_add_book_in_favorites_add_books_in_favorites(self, collector):
        books = ['Шерлок Холмс', 'Гарри Поттер', 'Сказка о царе салтане']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.favorites == ['Шерлок Холмс', 'Гарри Поттер', 'Сказка о царе салтане']

    def test_get_list_of_favorites_books_add_books_in_favorites(self, collector):
        books = ['Шерлок Холмс', 'Гарри Поттер', 'Сказка о царе салтане']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс', 'Гарри Поттер', 'Сказка о царе салтане']

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        books = ['Шерлок Холмс', 'Гарри Поттер', 'Сказка о царе салтане']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites('Шерлок Холмс')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Сказка о царе салтане']
