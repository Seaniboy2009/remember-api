from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for the profile model """

    # Changes the owner from ID to Username
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.ReadOnlyField(source='owner.username')

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = '__all__'