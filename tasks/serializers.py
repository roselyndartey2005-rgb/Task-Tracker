
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


    def validate_project(self, value):
        request = self.context.get("request")

        if request and value.owner != request.user:
            raise serializers.ValidationError(
                "You can only create tasks in your own projects."
            )

        return value
