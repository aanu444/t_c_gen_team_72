from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import t_c_Db
from django.http import HttpResponse


class CreateView(CreateView):  # Creates the view to insert text to database
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'home.html'
    success_url = 'list'


class ListTheView(ListView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    template_name = 'listView.html'


# Create your views here.


class UpdateTheView(UpdateView):  # list the texts inserted into the database into the html file created here
    model = t_c_Db
    fields = [
        "title", "description"
    ]
    template_name = 'Update.html'
    success_url = '/'


class DeleteTheView(DeleteView):
    model = t_c_Db
    template_name = 'Delete.html'
    success_url = '/'



# Create your views here.