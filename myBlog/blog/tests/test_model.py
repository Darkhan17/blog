
from blog.models import Author


from model_bakery import baker
import factory
import json
import pytest

from blog.models import Author


pytestmark = pytest.mark.django_db

class TestAuthorEndpoints:

    endpoint = '/API/authors/'

    def test_list(self, api_client):
        baker.make(Author, _quantity=3)

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        author = baker.prepare(Author)
        expected_json = {
            'name': author.name,
            'email': author.email,
            'password': author.password,
            'git_nickname': author.git_nickname
        }

        response = api_client().post(
            self.endpoint,
            data=expected_json,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client):
        author = baker.make(Author)
        expected_json = {
            'name': author.name,
            'email': author.email,
            'password': author.password,
            'git_nickname': author.git_nickname
        }
        url = f'{self.endpoint}{author.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, rf, api_client):
        old_author = baker.make(Author)
        new_author = baker.prepare(Author)

        author_dict = {
            'name': new_author.name,
            'email': new_author.email,
            'password': new_author.password,
            'git_nickname': new_author.git_nickname
        }

        url = f'{self.endpoint}{old_author.id}/'

        response = api_client().put(
            url,
            author_dict,
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content) == author_dict

    @pytest.mark.parametrize('field',[
        ('name'),
        ('email'),
        ('password'),
        ('git_nickname')
    ])
    def test_partial_update(self, mocker, rf, field, api_client):
        author = baker.make(Author)
        author_dict = {
            'code': author.code,
            'name': author.name,
            'symbol': author.symbol
        }
        valid_field = author_dict[field]
        url = f'{self.endpoint}{author.id}/'

        response = api_client().patch(
            url,
            {field: valid_field},
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, mocker, api_client):
        author = baker.make(Author)
        url = f'{self.endpoint}{author.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Author.objects.all().count() == 0