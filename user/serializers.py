from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[('Instructor', 'Instructor'), ('Student', 'Student')])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        role = validated_data.pop('role', None)

        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Assign the role
        if role:
            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)

        return user
