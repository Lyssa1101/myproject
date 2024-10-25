from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form_view, name='form_view'),
    path('data/', views.data_list, name='data_list'),
    path('data/<int:pk>/', views.detail_view, name='detail_view'),
]