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
    template_name = "leads/lead_list.html"
    fields = ['name', 'email', 'job']

    def get_success_url(self):
        return reverse_lazy('leads:lead_list')
    
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Lead.objects.all()
        return super(LeadCreate, self).get_context_data(**kwargs)
    
class LeadUpdate(UpdateView):
    model = Lead
    template_name = "leads/lead_list.html"
    fields = ['name', 'email', 'job']
    
    def get_success_url(self):
        return reverse_lazy('leads:lead_list')

        
class LeadDelete(DeleteView):
    model = Lead

    def get_success_url(self):
        return reverse_lazy('leads:lead_list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
