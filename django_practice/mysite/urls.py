from . import views
from django.urls import path

urlpatterns = [
    path('memos/', views.memo_list, name='memo_list'),
]


