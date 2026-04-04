from django.http import HttpResponse
from django.shortcuts import render

from elibrary_app.forms import AddBookForm
from elibrary_app.models import Catalog


def home(request):
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    else:
        add_book_form = AddBookForm()
    books = Catalog.objects.all()

    return render(request, 'elibrary/home.html', {
        "add_book_form": add_book_form,
        "books": books
    })