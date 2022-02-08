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

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email

    def create(self, validated_data):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not validated_data['email']:
            raise ValidationError('Users must have an email address')

        user = self.Meta.model(
            email=self.normalize_email(validated_data['email']),
            date_of_birth=validated_data['date_of_birth'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
