from rest_framework import serializers
from .models import Client
from users.serializers import UserSerializer
from .models import Client
from users.models import User

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        validated_data["user"] = user

        client = Client.objects.create(**validated_data)

        return client

    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop('user')
        except KeyError:
            request_user = False    

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
                instance.save()

        super().update(instance, validated_data)
        return instance
