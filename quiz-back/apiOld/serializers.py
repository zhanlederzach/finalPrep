from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from rest_framework import serializers
from apiOld import models
from apiOld.models import Post

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True)
#     body = serializers.CharField(required=True)
#     like_count = serializers.IntegerField()
#     # created_at = serializers.DateTimeField(default=datetime.now, blank=True)
#     # created_by = serializers.
#
#     def create(self, validated_data):
#         posts = Post(**validated_data)
#         posts.save()
#         return posts
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    like_count = serializers.IntegerField()
    # created_at = serializers.DateTimeField(required=True, input_formats=['%Y-%m-%d', ])

    # user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'like_count',)

    # def to_representation(self, instance):
    #     representation = super(TasksSerializer, self).to_representation(instance)
    #     representation['created_at'] = instance.created_at.strftime('YYYY-MM-DD')
    #     representation['due_on'] = instance.due_on.strftime('YYYY-MM-DD')
    #     return representation
