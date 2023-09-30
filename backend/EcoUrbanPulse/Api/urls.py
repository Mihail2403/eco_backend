from django.urls import path
from .views import register_user, login_user, auth_user, get_complaint, get_news, addComplain

urlpatterns = [
    path('register-user/', register_user),
    path('login_user/', login_user),
    path('auth_user/', auth_user),
    path('get-complaint/', get_complaint),
    path('get-news/', get_news),
    path('add-complain/', addComplain)
]
# ааа блять