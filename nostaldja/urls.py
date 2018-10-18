from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('decades/', views.decade_list, name='decade_list'),
    path('decades/<int:id>', views.decade_detail, name='decade_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('decades/<int:id>/edit', views.decade_edit, name='decade_edit'),
    path('decades/<int:id>/delete', views.decade_delete, name='decade_delete'),
    path('fads/', views.fad_list, name='fad_list'),
    path('fads/<int:id>', views.fad_detail, name='fad_detail'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('fads/<int:id>/edit', views.fad_edit, name='fad_edit'),
    path('fads/<int:id>/delete', views.fad_delete, name='fad_delete'),

]
