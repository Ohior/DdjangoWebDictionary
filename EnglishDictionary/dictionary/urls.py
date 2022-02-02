
from . import views
from django.urls import  path

urlpatterns = [
    path('', view=views.index, name='index'),
    path('word/', view=views.word, name='word'),
]