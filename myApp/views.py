from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Notes
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.



def index(request):
    return render(request, 'index.html')


class NotesDetail(DetailView):
    model = Notes
    template_name = 'notes_detail.html'

class NotesListView(ListView):
    model = Notes
    template_name = 'notes_list.html'