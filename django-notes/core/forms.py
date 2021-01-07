from django import forms
from .models import Note, Label

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = [
      'title',
      'body',
      'labels',
    ]

    title = forms.CharField()
    body = forms.Textarea()

    #labels = forms.ModelMultipleChoiceField(queryset=Label.objects.all(), widget=forms.CheckboxSelectMultiple)

class SearchForm(forms.Form):
  search_term = forms.CharField(label='Search Term', max_length=50, required=False)

