from django.shortcuts import render
from .converters import DateConverter

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_on_date(request, pub_date):
    template = 'books/books_on_date.html'
    converter = DateConverter()
    try:
        current_date = converter.to_python(value=pub_date)
        books = Book.objects.filter(pub_date=current_date)
        next_books = Book.objects.filter(pub_date__gt=current_date).order_by('pub_date')
        prev_books = Book.objects.filter(pub_date__lt=current_date).order_by('-pub_date')
        next_date = next_books[0].pub_date if next_books else None
        prev_date = prev_books[0].pub_date if prev_books else None
    except ValueError:
        books = None
        current_date = None
        prev_date = None
        all_books = Book.objects.order_by('pub_date')
        next_date = all_books[0].pub_date if all_books else None
    context = {
            'books': books,
            'next_date': next_date,
            'prev_date': prev_date,
            'current_date': current_date,
              }
    return render(request, template, context)