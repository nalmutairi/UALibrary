import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","booklibrary.settings")

import django
django.setup()


from books.models import Book, Publisher, Title, Category, Place


def get_file_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid File Path: {}".format(file_path))
    return file_path


def read_data(path):
    Book.objects.all().delete()
    file = get_file_path(path)
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['\ufeffName']
            author = row['Author']
            cat = row['CatID']
            pub = row['PubID']
            title = row['TitleID']
            place = row['PlaceID']
            pages = 0 if row['Pages'] == "NULL" or row['Pages'] == "" else row['Pages']
            press = row['Press']
            parts = 0 if row['Parts'] == "NULL" or row['Parts'] == "" else row['Parts']
            notes = row['Notes']

            book = Book.objects.create(
                name = name,
                author= author,
                pages=pages,
                press=press,
                parts=parts,
                notes=notes
            )

            try:
                publisher = Publisher.objects.get(id=pub)
                book.publisher=publisher
            except:
                print("Pub: " + pub)

            try:
                title = Title.objects.get(id=title)
                book.title = title
            except:
                print("Title: " + title)


            try:
                place = Place.objects.get(id=place)
                book.place = place
            except:
                print("Place: " + place)

            try:
                category = Category.objects.get(id=cat)
                book.cat = category
            except:
                print("Cat: " + cat)




            # title = Title.objects.get(id=title)
            # place = Place.objects.get(id=place)
            # category = Category.objects.get(id=cat)


            book.save()


read_data('book.csv')

