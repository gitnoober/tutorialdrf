from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.ListUser.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

# dont need to add this but this refers to simple clean urls (here format is None)
urlpatterns = format_suffix_patterns(urlpatterns)
