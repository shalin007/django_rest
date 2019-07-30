from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer




class StatusSerializer(serializers.ModelSerializer):
    user=UserPublicSerializer(read_only=True)
    class Meta:
        model =Status
        fields=[
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields=['user']