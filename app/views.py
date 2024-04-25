from django.shortcuts import render, redirect, get_object_or_404
from . models import Folder, Image
from .forms import FolderForm, ImageForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def welcome(request):
    if request.user.is_authenticated:
        return redirect('gallery')
    
    return render(request, 'app/welcome.html')

@login_required(login_url='login')
def gallery(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    folders = Folder.objects.filter(user = request.user)
    images = Image.objects.filter(user = request.user, tag__icontains = q)

    image_exists = Image.objects.filter(user = request.user).exists()

    context = {
        'folders': folders,
        'images': images,
        'image_exists': image_exists
    }

    return render(request, 'app/gallery.html', context)

@login_required(login_url='login')
def folders(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    folders = Folder.objects.filter(user = request.user, name__icontains = q)
    
    context = {
        'folders': folders,
    }

    return render(request, 'app/folders.html', context)

@login_required(login_url='login')
def upload(request):
    form = ImageForm()
    folders = Folder.objects.filter(user = request.user)
    folder_exists = Folder.objects.filter(user = request.user).exists()

    if not folder_exists:
        return redirect('create-folder')
        
    else:
        page = 'upload'

    if request.method == 'POST':
        folder = request.POST.get('folder')
        image = request.FILES.get('image')
        tag = request.POST.get('tag')
        
        image = Image.objects.create(
            user = request.user,
            folder = Folder.objects.get(user = request.user, name = folder),
            image = image,
            tag = tag,
                            )
        image.save()
        return redirect('gallery')
    context = {
        'page': page,
        'folders': folders,
        
    }
    return render(request, 'app/upload.html', context)

@login_required(login_url='login')
def create_folder(request):
    form = FolderForm()
    page = 'create_folder'
    folders = Folder.objects.filter(user = request.user).exists

    if request.method == 'POST':
        name = request.POST.get('name')

        folder = Folder.objects.create(
            user = request.user,
            name = name,
        )
        folder.save()
        return redirect('folders')
    context = {
        'page': page,
        'folders': folders,
        'form': form,
    }

    return render(request, 'app/upload.html', context)

@login_required(login_url='login')
def image_detail(request, pk):
    image =Image.objects.get(pk=pk)
    context = {
        'image': image
    }
    return render(request, 'app/imageDetail.html', context)

@login_required(login_url='login')
def folder(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    folder = Folder.objects.get(pk=pk)
    images = Image.objects.filter(user = request.user, folder = folder, tag__icontains = q)
    # images = Image.objects.filter(user = request.user, )
    image_exists = Image.objects.filter(user = request.user, folder = folder).exists()

    context = {
        'images': images,
        'image_exists': image_exists,
        'folder': folder,
    }
    return render(request, 'app/folder.html', context)

@login_required(login_url='login')
def delete_folder(request, pk):
    obj = Folder.objects.get(pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('folders')

    context = {
        'obj': 'folder'
    }
    return render(request, 'app/delete.html', context)

@login_required(login_url='login')
def delete_image(request, pk):
    obj = Image.objects.get(pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('gallery')

    context = {
        'obj': 'image'
    }
    return render(request, 'app/delete.html', context)

def rename_image(request, pk):
    image = Image.objects.get(pk=pk)

    if request.method == "POST":
        tag = request.POST.get('name')

        image.tag = tag
        image.save()
        return redirect('image', pk=image.id)

    context = {
        'image': image,
        'obj': 'image'
    } 
    return render(request, 'app/rename.html', context)

def rename_folder(request, pk):
    folder = Folder.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST.get('name')
        folder.name = name
        folder.save()
        return redirect('folder', pk=folder.id)

    context = {
        'folder': folder,
        'obj': 'folder'
    } 
    return render(request, 'app/rename.html', context)

