from django.core.paginator import Paginator
from django.http import Http404
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
    books = None
    current_date = None
    next_date = None
    prev_date = None
    try:
        all_books = Book.objects.order_by('pub_date')
        current_date = converter.to_python(value=pub_date).date()
        all_pub_dates = all_books.values_list('pub_date', flat=True).distinct()
        next_pub_dates = all_pub_dates.filter(pub_date__gt=current_date)
        prev_pub_dates = all_pub_dates.filter(pub_date__lt=current_date).order_by('-pub_date')
        if next_pub_dates:
            next_date = next_pub_dates[0]
        if prev_pub_dates:
            prev_date = prev_pub_dates[0]
        books = all_books.filter(pub_date=current_date)
    except ValueError:
        current_date = None
    context = {
            'books': books,
            'current_date': current_date,
            'next_date': next_date,
            'prev_date': prev_date,
              }
    return render(request, template, context)