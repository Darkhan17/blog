from celery import shared_task

from .models import Project,Author
from celery import shared_task
import requests


@shared_task
def create_project():
    authors = Author.objects.all()
    authors_git_nicknames = [author.git_nickname for author in authors]
    for nickname in  authors_git_nicknames:
        response = requests.get("https://api.github.com/users/{0}/repos".format(nickname))
        if response.status_code == 200:
            for content in response.json():
                id = content['id']
                title = content['name']
                description = content['description']
                url = content['url']
                if description is None:
                    description = "No description"
                project, created = Project.objects.get_or_create(
                    id = id,
                    title = title,
                    description = description,
                    url = url,
                    author = Author.objects.get(git_nickname = nickname)
                )
