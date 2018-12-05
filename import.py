import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","booklibrary.settings")

import django
django.setup()


from books.models import Category


def get_file_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid File Path: {}".format(file_path))
    return file_path


def read_data(path):
    file = get_file_path(path)
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['\ufeffName']
            Category.objects.create(name = name)


read_data('cat.csv')

