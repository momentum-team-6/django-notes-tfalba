from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Label
from .data import NOTES
from .forms import NoteForm, SearchForm
import requests

def list_notes(request):
  labels = Label.objects.all()
  if request.method == 'POST':
    form = SearchForm(data=request.POST)
    if form.is_valid():
      my_search_term = form.data['search_term']
      notes = Note.objects.filter(body__icontains=my_search_term)
  elif request.GET.get('labels'):
    form = SearchForm()
    select_label = request.GET.get('labels')
    if select_label == 'All':
      notes = Note.objects.all()
    else:
      notes = Note.objects.filter(labels__name=select_label)
  else:
    form = SearchForm()
    notes = Note.objects.all()
  return render(request, 'notes/index.html', {"notes": notes, "form": form, "labels": labels})


def note_detail(request, pk):
  note = get_object_or_404(Note, pk=pk)
  labels = Label.objects.filter(notes=note)
  return render(request, "notes/note_detail.html", {"note": note, "labels": labels})

def add_note(request):
  if request.method == 'GET':
    form = NoteForm()
  else:
    form = NoteForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect(to='notes_list')
  return render(request, "notes/add_note.html", {"form": form })

def edit_note(request, pk):
  note = get_object_or_404(Note, pk=pk)
  if request.method == 'GET':
    form = NoteForm(instance=note)
  else:
    form = NoteForm(data=request.POST, instance=note)
    if form.is_valid():
      form.save()
      return redirect(to='notes_list')
  return render(request, "notes/edit_note.html", {
    "form": form,
    "note": note
  })

def delete_note(request, pk):
  note = get_object_or_404(Note, pk=pk)
  if request.method == 'POST':
    note.delete()
    return redirect(to='notes_list')
  return render(request, "notes/delete_note.html", {
    "note": note
  })


def label_filter(request):

  pass

