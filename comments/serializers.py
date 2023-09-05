from rest_framework import serializers
from .models import Comments
from users.models import User
from movies.models import Movies
from users.serializers import UserSerializer
from movies.serializers import MovieSerializer
from django.shortcuts import get_object_or_404


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)

    movie = MovieSerializer(read_only=True)
    movie_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Comments
        fields = ['id','content','user','user_id','movie','movie_id']
        read_only_fields = ['id']


    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(User, id = user_id)

        movie_id = validated_data.pop('movie_id')
        movie_found = get_object_or_404(Movies, id = movie_id)

        new_comment = Comments.objects.create(**validated_data, user=user_found, movie=movie_found)

        return new_comment
    

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        super().update(instance, validated_data)
        return instance
        