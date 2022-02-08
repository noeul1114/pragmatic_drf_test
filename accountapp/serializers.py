from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from accountapp.models import PragmaticUser


class PragmaticUserSerializer(HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = PragmaticUser
        fields = ('email', 'date_of_birth', 'password')

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)
