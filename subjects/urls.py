from django.urls import path,re_path
from . import views
from django.views.generic.base import TemplateView

from django.contrib import admin

app_name='subjects'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_subject/', views.Add_SubjectView.as_view(), name='add_subject'), # new
    path('upload_file/', views.UploadFileView.as_view(), name='upload_file'), # new
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
    path('<int:pk>/', views.NotesView.as_view()),
]