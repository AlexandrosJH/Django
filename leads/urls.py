from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
  path('', views.LeadCreate.as_view(), name='lead_list'),
  path('new', views.LeadCreate.as_view(), name='lead_new'),
  path('edit/<int:pk>/', views.LeadUpdate.as_view(), name='lead_edit'),
  path('delete/<int:pk>/', views.LeadDelete.as_view(), name='lead_delete'),
]