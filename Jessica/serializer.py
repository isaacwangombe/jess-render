from rest_framework import serializers
from .models import Comments, Projects, Tools, Models



class ModelsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Models
    fields = ('id','name')


class ToolsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tools
    fields = ('id','name')


class CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = ('name', 'email',  'comment', 'rating','date', 'project')


class ProjectSerializer(serializers.ModelSerializer):

  tools = ToolsSerializer(many=True)
  models = ModelsSerializer(many=True)

  class Meta:
    model = Projects
    fields = ('id','name', 'details','highlighted', 'date', 'tools', 'models', 'image','github')

