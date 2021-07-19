from django.urls import path
from .views import BlogAPIView,ProjectAPIView,AuthorAPIView, AuthorList,ProjectList,BlogList, getMyBlogs


from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogAPIView.as_view()),
   # path('myBlogs/', getMyBlogs),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>', AuthorAPIView.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectAPIView.as_view()),
]