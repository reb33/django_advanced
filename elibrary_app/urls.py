from django.urls import path

from elibrary_app.views import home

urlpatterns = [
    path('', home, name='home')
]