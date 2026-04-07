from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.utils.translation import gettext_lazy as _

from books.forms import BookCreateForm, BookEditForm
from books.models import Book


def delete_cache_keys():
    key_list = []
    for col in ('pk', 'title', 'author', 'price', 'read'):
        key_list += ['cached_book_list_sorted_' + col]
        key_list += ['cached_book_list_sorted_-' + col]
    cache.delete_many(key_list)


@require_http_methods(["GET"])
def book_list(request):
    books = cache.get_or_set('cached_book_list_sorted_pk', Book.objects.all())
    form = BookCreateForm(auto_id=False)
    return render(request, 'books/base.html', {'book_list': books, 'form': form})


@require_http_methods(["POST"])
def book_create(request):
    form = BookCreateForm(request.POST)
    book = None
    if form.is_valid():
        book = form.save()
        delete_cache_keys()
    return render(request, 'books/partial_book_detail.html', {'book': book})


def update_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            delete_cache_keys()
            return render(
                request,
                'books/partial_book_detail.html',
                {'book': book}
            )
    else:
        form = BookEditForm(instance=book)
    return render(
        request,
        'books/partial_book_update_form.html',
        {'book': book, 'form': form}
    )


@require_http_methods(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
        'books/partial_book_detail.html',
        {'book': book}
    )


@require_http_methods(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    delete_cache_keys()
    return HttpResponse()


@require_http_methods(['PATCH'])
def update_book_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.read = not book.read
    book.save()
    delete_cache_keys()
    return render(
        request,
        'books/partial_book_detail.html',
        {'book': book}
    )


@require_http_methods(['GET'])
def book_list_sort(request, filter, direction):
    filter_dict = {
        _('id'): 'pk',
        _('title'): 'title',
        _('author'): 'author',
        _('price'): 'price',
        _('read'): 'read',
    }
    if filter in filter_dict:
        sort_str = ('', '-')[direction == _('descend')] + filter_dict[filter]
    else:
        sort_str = 'pk'
    cache_key = 'cached_book_list_sorted_' + sort_str
    books = cache.get_or_set(cache_key, Book.objects.order_by(sort_str))
    return render(
        request,
        'books/partial_book_list.html',
        {'book_list': books}
    )