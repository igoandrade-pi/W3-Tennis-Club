from django.urls import path
from . import views

app_name='members'
urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.list_view, name='list_view'),
    path('members/details/<int:id>', views.detail_view, name='detail_view'),
    path('members/delete/<int:id>', views.delete_view, name='delete_view'),
]