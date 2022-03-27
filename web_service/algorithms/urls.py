""" Algorithms URLs """
from django.urls import path

from algorithms.views.fibonacci import Fibonacci
from algorithms.views.ackermann import Ackermann
from algorithms.views.factorial import Factorial

urlpatterns = [
    path('fibonacci/', Fibonacci.as_view()),
    path('ackermann/', Ackermann.as_view()),
    path('factorial/', Factorial.as_view()),
]
