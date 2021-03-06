
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegisterView,LogoutView



urlpatterns = [
    path('login/',obtain_jwt_token),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView),
]