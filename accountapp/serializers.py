from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

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
        fields = ('url', 'email', 'date_of_birth', 'password')

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        if validated_data.get('password') is not None:
            instance.set_password(validated_data['password'])

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance


class PragmaticUserSerializerWithoutEmail(HyperlinkedModelSerializer):
    class Meta:
        model = PragmaticUser
        fields = ('url', 'date_of_birth')



