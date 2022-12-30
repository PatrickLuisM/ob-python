from django.shortcuts import render

# Create your views here.

from .models import Book,Author,BookInstance,Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.all().count()


    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_authors': num_author,
            'disponibles': disponibles,
            'num_instances':num_instances
        }
    )