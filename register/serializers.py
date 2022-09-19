from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_no = serializers.IntegerField()
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)