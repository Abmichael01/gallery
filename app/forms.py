from django.forms import ModelForm
from . models import Folder, Image

class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['user','name']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['user','tag', 'image', 'folder']