from django.urls import path
from .views import links

urlpatterns = [
    path('link/$', links)
]