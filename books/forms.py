from dal import autocomplete
from django import forms
from .models import Book, Publisher, Category, Title, Place


class BookForm2(forms.Form):
	name = forms.CharField()
	author = forms.CharField()
	publisher = forms.CharField()
	title = forms.CharField()
	place = forms.CharField()
	category = forms.CharField()
	pages = forms.IntegerField()
	press = forms.CharField()
	parts = forms.IntegerField()
	notes = forms.CharField()

	widgets = {
		'publisher': autocomplete.ModelSelect2(url = 'publisher-autocomplete')
	}