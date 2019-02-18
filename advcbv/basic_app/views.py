from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from . import models

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    # def get_context_data(self,**kwargs):
    #     context  = super().get_context_data(**kwargs)
    #     context['injectme'] = "Basic Injection!"
    #     return context

class SchoolListView(ListView):
    context_object_name='schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    print('inside detail view')
    context_object_name='school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'



class SchoolDeleteView(DeleteView):
    model=models.School
    success_url= reverse_lazy("basic_app:list")

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model=models.School
