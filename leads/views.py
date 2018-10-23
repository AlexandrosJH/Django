from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from leads.models import Lead

# Create your views here.

class LeadList(ListView):
    model = Lead

class LeadCreate(CreateView):
    model = Lead
    fields = ['name', 'email', 'job']
    success_url = reverse_lazy('leads:lead_list')
    
class LeadUpdate(UpdateView):
    model = Lead
    fields = ['name', 'email', 'job']
    success_url = reverse_lazy('leads:lead_list')
    
class LeadDelete(DeleteView):
    model = Lead
    fields = ['name', 'email', 'job']
    success_url = reverse_lazy('leads:lead_list')

