from django.urls import path,re_path
from . import views
from django.views.generic.base import TemplateView

from django.contrib import admin

app_name='subjects'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Add_SubjectView.as_view(), name='add_subject'), # new
    path('<int:pk>/', views.NotesView.as_view()),
]