from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Comments, Models, Tools
from .serializer import ProjectSerializer, CommentsSerializer, ModelsSerializer, ToolsSerializer
from django.http import Http404
from rest_framework import status


class ProjectList(APIView):
	def get(self, request, format=None):
		all_projects = Projects.get_all()
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)


class ProjectById(APIView):
	def get(self, request, id,format=None):
		all_projects = Projects.get_id(id)
		serializers = ProjectSerializer(all_projects, many=False)
		return Response(serializers.data)


class ProjectByModels(APIView):
	def get(self, request, models,format=None):
		all_projects = Projects.filter_tool(models)
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)


class ProjectByTools(APIView):
	def get(self, request, tools,format=None):
		all_projects = Projects.filter_model(tools)
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)



class ToolsList(APIView):
	def get(self, request, format=None):
		all_items = Tools.get_all()
		serializers = ToolsSerializer(all_items, many=True)
		return Response(serializers.data)


class ModelsList(APIView):
	def get(self, request, format=None):
		all_items = Models.get_all()
		serializers = ModelsSerializer(all_items, many=True)
		return Response(serializers.data)



class CommentsList(APIView):
	def get(self, request,format=None):
		all_comments = Comments.get_all()
		serializers = CommentsSerializer(all_comments, many=True)
		return Response(serializers.data)

	def post(self, request, format=None):
			serializers = CommentsSerializer(data=request.data)
			if serializers.is_valid():
					serializers.save()
					return Response(serializers.data, status=status.HTTP_201_CREATED)
			return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)