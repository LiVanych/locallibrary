from django.test import TestCase

from catalog.models import Author, Book, Language, Genre, BookInstance

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Genre.objects.create(name='Fantazy')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = genre.name
        self.assertEquals(expected_object_name, str(genre))

class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Language.objects.create(name='English')

    def test_name_label(self):
        lang = Language.objects.get(id=1)
        field_label = lang._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        lang = Language.objects.get(id=1)
        max_length = lang._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        lang = Language.objects.get(id=1)
        expected_object_name = lang.name
        self.assertEquals(expected_object_name, str(lang))

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')
        author_name = Author.objects.get(id=1)
        Language.objects.create(name='English')
        lang_name = Language.objects.get(id=1)
        Genre.objects.create(name='Fiction')
        genre_name = Genre.objects.get(id=1)
        book = Book.objects.create(
                     title='Test Book title',
                     author=author_name,
                     language=lang_name,
                     summary='This is the very nice book',
                     isbn='9876543212345'
                     )
        book.genre.add(genre_name)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_genre_label(self):
        book =  Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_author_label(self):
        book =  Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_language_label(self):
        book =  Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    def test_summary_label(self):
        book =  Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        book =  Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')

class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Author.objects.create(first_name='Big', last_name='Bob')
        author_of_book = Author.objects.get(id=1)
        Language.objects.create(name='English')
        lang_of_book = Language.objects.get(id=1)
        Genre.objects.create(name='Fiction')
        genre_of_book = Genre.objects.get(id=1)
        book = Book.objects.create(
                     title='Test Book title',
                     author=author_of_book,
                     language=lang_of_book,
                     summary='This is the very nice book',
                     isbn='9876543212345'
                     )
        # ManyToManyField type of field in model
        book.genre.add(genre_of_book)
        first_book = Book.objects.first()
        book_instance = BookInstance.objects.create(
                     book=first_book,
                     imprint='Published by Self-published Print',
                     status='a'
                     )

    def test_id_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_book_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('book').verbose_name
        self.assertEquals(field_label, 'book')

    def test_due_back_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('due_back').verbose_name
        self.assertEquals(field_label, 'due back')

    def test_borrower_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('borrower').verbose_name
        self.assertEquals(field_label, 'borrower')

    def test_status_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_imprint_label(self):
        book_inst = BookInstance.objects.first()
        field_label = book_inst._meta.get_field('imprint').verbose_name
        self.assertEquals(field_label, 'imprint')

    def test_imprint_max_length(self):
        book_inst = BookInstance.objects.first()
        max_length = book_inst._meta.get_field('imprint').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_id_book_title(self):
        book_inst = BookInstance.objects.first()
        expected_object_name = f'{book_inst.id} ({book_inst.book})'
        self.assertEquals(
                          expected_object_name,
                          str(book_inst.id) + ' ' + '('+str(book_inst.book)+')')
