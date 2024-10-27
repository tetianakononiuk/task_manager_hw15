from rest_framework import serializers
from my_app.models.task import SubTask, Category, Task
from rest_framework.exceptions import ValidationError
from django.utils import timezone




class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['title', 'description', 'task', 'deadline', 'status', 'created_at']
        read_only_fields = ['created_at']

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

def validate_name(self, value):
    if Category.objects.filter(name=value).exists():
        raise ValidationError('Category with this name already exists.')
    return value

def create(self, validated_date):
    name = validated_date.get('name')
    if Category.objects.filter(name=name).exists():
        raise ValidationError('Category with this name already exists.')
    return super().create(validated_date)

def update(self, instance, validated_data):
    name = validated_data.get('name', instance.name)
    if Category.objects.filter(name=name).exists():
        raise ValidationError('Category with this name already exists.')
    return super().update(instance, validated_data)


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id','title', 'description', 'status', 'deadline']



class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description','status','deadline', 'created_at', 'subtasks']



class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise ValidationError('The deadline cannot be in the past.')
        return value



