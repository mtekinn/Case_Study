from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import NotesDetail, NotesListView


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', NotesDetail.as_view(), name='notes_detail'),
    path('', NotesListView.as_view(), name='notes_list'),
]
