from .models import Profile,CustomResponse
from rest_framework import serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'phone_number',
            'address',
        ]
class CustomResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomResponse
        fields = ["message","token"]
    def to_representation(self,instance):
        data = super().to_representation(instance)
        if not data["token"]:
            del data["token"]
        return data