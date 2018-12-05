from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from dal import autocomplete
from .models import Place, Publisher, Title, Category, Book
from .forms import BookForm2



def book_list(request):
    context = {
        "books" : Book.objects.all(),
    }
    return render(request, 'booklist.html', context)

def pub_list():
    query_set = Publisher.objects.all()
    query_set = serializers.serialize('json' , query_set)
    return query_set


def book_create(request):
    form = BookForm2()
    if request.method == "POST":
        form = BookForm2(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            publisher = form.cleaned_data['publisher']
            parts = form.cleaned_data['parts']
            category = form.cleaned_data['category']
            title = form.cleaned_data['title']
            place = form.cleaned_data['place']
            notes = form.cleaned_data['notes']
            pages = form.cleaned_data['pages']
            press = form.cleaned_data['press']
            publisher_obj, created = Publisher.objects.get_or_create(publishername=publisher)
            place_obj, created = Place.objects.get_or_create(placename=place)
            title_obj, created = Title.objects.get_or_create(titlename=title)
            category_obj, created = Category.objects.get_or_create(categoryname=category)
            Book.objects.create(
                name = name,
                author = author,
                publisher = publisher_obj,
                parts = parts,
                category = category_obj,
                title = title_obj,
                place = place_obj,
                notes = notes,
                pages = pages,
                )



    serialized_obj = pub_list()
    

    pub = list(Publisher.objects.values())
    pubs = [publisher.publishername for publisher in Publisher.objects.all()]

    context = {
    "form" : form,
    "publishers" : serialized_obj,
    }
    
    
    return render(request, 'createbook2.html' , context)









