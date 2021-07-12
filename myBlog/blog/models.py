from django.db import models

from django.contrib.auth.models import AbstractUser



class Author(AbstractUser):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=255, default='')
    password = models.CharField(max_length=200)
    git_nickname = models.CharField(max_length=200, blank=True
                                    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email



class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    url = models.CharField(max_length=200)
    author  = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
