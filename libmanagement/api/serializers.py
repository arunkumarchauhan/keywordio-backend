from rest_framework import serializers
from .models import User,Book

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "is_staff"
        ]
        extra_kwargs = {"password": {"write_only": True},'is_staff':{"write_only":True}}

    def create(self, validated_data):
        username = validated_data["name"]
        email = validated_data["email"]
        password = validated_data["password"]
        is_staff=validated_data['is_staff']
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        user = User(name=username, email=email,is_staff=is_staff)
        user.set_password(password)
        user.save()
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class GetBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at','modified_at']