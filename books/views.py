from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from .forms import BookForm, CategoryForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def book_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'date_added')
    books = Book.objects.all()

    if sort_by.endswith('_desc'):
        sort_by = '-' + sort_by[:-5]

    if query:
        books = books.filter(Q(title__icontains=query) | Q(category__name__icontains=query) | Q(date_added__icontains=query))
    else:
        query = ''

    books = books.order_by(sort_by)
    paginator = Paginator(books, 4)  # 10 книг на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book_list.html', {'page_obj': page_obj, 'query': query, 'sort_by': sort_by})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'category_list.html', {'categories': categories})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')
