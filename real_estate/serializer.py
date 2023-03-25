from real_estate.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.utils.translation import gettext_lazy as _


# User serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", "")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        email = attrs.get("email", " ")
        username = attrs.get("username", " ")
        password = attrs.get("password", " ")
        if email is None:
            raise serializers.ValidationError("user must have email")
        if username is None:
            raise serializers.ValidationError("user must have username")

        if len(password) < 4:
            raise serializers.ValidationError("password must be longer than 6")
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RefreshtokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=255)

    default_error_messages = {"bad_token": _("Token is invalid / expired")}

    def validate(self, attrs):
        self.token = attrs.get("refresh", "")
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
