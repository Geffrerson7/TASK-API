from rest_framework import serializers
from .models import Task
from user.serializer import UserSerializer

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = 'user',
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('request').method in ['GET']:
            user = UserSerializer(instance.user).data
            representation['user'] = user
            
        return representation