from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError, EmailField
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterSerializer(ModelSerializer):
    email = EmailField(label="Email address")
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]

    extra_kwargs = {
        "password":
            {"write_only":True},
        "id":
            {"read_only":True}
    }

    def validate(self, data):
        return data

    def validate_email(self, value):
        email = value
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Email already registered")
        return value

    def create(self, validate_data):
        username = validate_data['username']
        password = validate_data['password']
        email = validate_data['email']
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        users = User.objects.all()
        tokens = Token.objects.all()

        user_id = None
        token_user = []

        for token in tokens:
            token_user.append(token.user_id)
        
        for user in users:
            userid = user.id
            if userid not in token_user:
                get_user = User.objects.get(id=userid)
                save_token = Token(user=get_user)
                save_token.save()

        return user_obj

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')