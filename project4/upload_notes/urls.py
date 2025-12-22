from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('upload/', views.note_upload, name='note_upload'),
]
