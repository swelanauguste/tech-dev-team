from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import DayIn

class DayInListView(ListView):
    model = DayIn