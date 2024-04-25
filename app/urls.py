from django.urls import path
from . views import *

urlpatterns = [
    path('', welcome, name="welcome"),
    path('gallery/', gallery, name="gallery"),
    path('folders/', folders, name="folders"),
    path('upload/', upload, name="upload"),
    path('create-folder/', create_folder, name="create-folder"),
    path('image/<str:pk>/', image_detail, name="image"),
    path('folder/<str:pk>/', folder, name="folder"),
    path('delete-image/<str:pk>/', delete_image, name="delete-image"),
    path('delete-folder/<str:pk>/', delete_folder, name="delete-folder"),
    path('rename-folder/<str:pk>/', rename_folder, name="rename-folder"),
    path('rename-image/<str:pk>/', rename_image, name="rename-image"),
]
