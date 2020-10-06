from django.test import Client, TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Hunger Games',
            author='Suzzane Collins',
            price='38',
        )
    
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}','Hunger Games')
        self.assertEqual(f'{self.book.author}','Suzzane Collins')
        self.assertEqual(f'{self.book.price}', '38')
    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Hunger Games')
        self.assertTemplateUsed(response, 'books/book_list.html')

    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Hunger Games')
        self.assertTemplateUsed(response, 'books/book_detail.html')
