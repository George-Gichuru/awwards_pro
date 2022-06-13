from rest_framework.serializers import ModelSerializer
from project.models import Post, Profile

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'name', 'country', 'prof_pic' ]
