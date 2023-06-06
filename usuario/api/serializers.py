from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class UsuarioSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ['foto', 'nome', 'sobrenome', 'username', 'email', 'celular']


class CriarUsuarioSerializer(ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'username', 'celular', 'email', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class ChangePasswordSerializer(serializers.Serializer):
    model = Usuario

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
