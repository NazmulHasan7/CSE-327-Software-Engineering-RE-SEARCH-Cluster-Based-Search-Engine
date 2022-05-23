from base_app.models import Cluster, Url
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from rest_framework.serializers import (
	ModelSerializer,
	ValidationError,
	EmailField,
)


# serializer classes for the models
class cluster_serializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = Cluster
        fields = ('user', 'title', 'description', 'date_updated', 'slug')

class url_serializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = Url
        fields = ('cluster', 'cluster_url', 'depth' ,'output_type' ,'date_added' ,'slug' )


""" class user_serializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'is_active', 'date_joined')

 """

#serializer for authentication

class RegisterSerializer(ModelSerializer):
	email = EmailField(label='Email adress')
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'password',
			'email',
		]
	extra_kwargs = {"password":
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
			raise ValidationError("Email alredy registred")
		return value


	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		user_obj = User(
			username = username,
			email = email,
		)
		user_obj.set_password(password)
		user_obj.save()
		return user_obj