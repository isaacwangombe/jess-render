from django.urls import path, include
from . import views, api_views



urlpatterns = [
  path('', views.welcome,name = 'test'),


  path('api/all_projects/', api_views.ProjectList.as_view()),
  path('api/all_tools/', api_views.ToolsList.as_view()),
  path('api/all_models/', api_views.ModelsList.as_view()),
  path('api/all_comments/', api_views.CommentsList.as_view()),

  path('api/id_projects/<id>', api_views.ProjectById.as_view()),
  path('api/model_projects/<models>', api_views.ProjectByModels.as_view()),
  path('api/tool_projects/<tools>', api_views.ProjectByTools.as_view()),


]
