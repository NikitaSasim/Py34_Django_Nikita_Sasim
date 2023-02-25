from django.test import TestCase
from .models import Author, Book, Genre
from django.contrib.auth.models import User
from django.urls import reverse


class MyTestClass(TestCase):
    def setUp(self) -> None:
        # Установки, которые запускаются перед каждым тестом
        pass

    def tearDown(self) -> None:
        # Очистка после каждого метода
        pass

    def test_that_will_pass(self):
        self.assertFalse((2 + 2) == 5)

    # def test_that_will_fail(self):
    #     self.assertTrue((2 + 2) == 5)

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name="Lorem", last_name="Ipsum")


    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_name = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_name, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_name = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_name, 'last name')


    def test_get_author_urll(self):
        author = Author.objects.get(id=1)
        expected_url = f"/authors/{author.first_name}-{author.last_name}-{author.id}/"
        self.assertEquals(expected_url, author.get_author_url())

class CatalogViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("test", "test@test.test", "1234")
        author = Author.objects.create(first_name="Lorem", last_name="Ipsum")
        genre = Genre.objects.create(name="test")
        book = Book.objects.create(title="Test", summary="Test", amount=1, author=author).genre.add(genre)

    def test_view_url_catalog_index(self):
        url = reverse("catalog-index")
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/catalog.html')

    def test_view_url_catalog_book(self):
        url = reverse("catalog-book", args=[1])
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/book.html')


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("test", "test@test.test", "1234")

    def test_view_url_login(self):
        url = reverse("login")
        data = {
            'username': "test",
            'password': "1234"
        }

        resp = self.client.post(url, data=data)

        self.assertEquals(resp.status_code, 302)