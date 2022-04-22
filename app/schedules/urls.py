from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.DayInListView.as_view(), name='dayin-list'),
]
