from blog.models import Author,Project,Blog

from .permissions import OwnBlogPermission, OwnProfilePermission


from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .utils import ViewListMixin

from .serializers import BlogSerializer,AuthorSerializer,ProjectSerializer
from rest_framework.decorators import api_view
# Create your views here.







@api_view(['GET'])
def getMyBlogs(request,user):
    blogs = Blog.objects.filter(user = user)
    serializer = BlogSerializer(data=blogs,many=True)
    return Response(serializer.data)


class ProjectList(ViewListMixin):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer




class BlogList(ViewListMixin):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class AuthorList(ViewListMixin):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorAPIView(APIView):

    permission_classes = [OwnProfilePermission, ]

    def get_author(self, pk):
        try:
            author = Author.objects.get(id = pk)
            return author
        except Author.DoesNotExist as error:
            raise Http404

    def get(self, request, pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_author(pk)
        author.delete()
        return Response(status=204)


class BlogAPIView(APIView):

    permission_classes = [OwnBlogPermission,]

    def get_object(self, pk):
        try:
            blog = Blog.objects.get(id = pk)
            return blog
        except Blog.DoesNotExist as error:
            raise Http404

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog= self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=204)


class ProjectAPIView(APIView):
    permission_classes = [IsAuthenticated, OwnBlogPermission]

    def get_object(self, pk):
        try:
            blog = Project.objects.get(id = pk)
            return blog
        except Project.DoesNotExist as error:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

