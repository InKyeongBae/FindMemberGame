from django.urls import path
from piroquiz.views import *

app_name = 'piroquiz'

urlpatterns = [
    path('', beforehome, name='beforehome'),
    path('create/', CreateQuiz, name='CreateQuiz'),
    path('list/', index, name='index'),
    path('quiz/<int:pk>/', SolveQuiz, name='SolveQuiz'),
    path('delete/<int:pk>/', DeleteQuiz, name='DeleteQuiz'),
]
