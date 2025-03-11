from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()  # ✅ Dynamically determine role

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'address', 'role']

    def get_role(self, obj):
        return "admin" if obj.is_staff else "standard"  # ✅ Check if user is admin

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone', 'address', 'role']

    def create(self, validated_data):
        role = validated_data.pop("role", "standard").lower()  # Extract role (default to standard)
        is_admin = role == "admin"  # Check if user should be admin

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            address=validated_data.get('address', ''),
            is_staff=is_admin  # ✅ Ensure admin users have is_staff=True
        )

        return user
