from django.urls import path

from items.views import item_view

urlpatterns = [
    path('items/<int:pk>/', item_view, name="item"),
]
