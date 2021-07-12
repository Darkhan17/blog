from blog.models import Author,Blog,Project
from rest_framework import serializers


class AuthorSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'email', 'git_name']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'





class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    blog_set = BlogSerializer(many=True, read_only=True)
    project_set = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'username', 'git_nickname', 'blog_set', 'project_set', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


