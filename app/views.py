from app import models
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm


def model_Form_Upload(request):

    form = DocumentForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()

        return redirect('app:feed')

    return render(request, 'app/upload.html', {'form': form})


def feed_Function(request):
    pictures = [{
        'url': picture.photo.url.replace('app/Static', ''),
        'id': picture.id
    }]
    return render(request, 'app/feed.html', {'pictures': pictures})
