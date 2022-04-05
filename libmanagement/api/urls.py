from django.contrib import admin
from django.urls import path

from .views.book_view import AdminBookView,GetBookView
from .views.user_view import RegisterView,LoginView
urlpatterns = [
    path('user/register/<type>', RegisterView.as_view(),name='register_user_view'),
    path('book/all', GetBookView.as_view(),name='get_book_view'),
    path('user/login', LoginView.as_view(),name='login_user_view'),
    path('book', AdminBookView.as_view(),name='admin_book_view'),
    path('book/<id>', AdminBookView.as_view(),name='admin_book_view'),

]