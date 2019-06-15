from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DownloadForm
from .models import Download
from .tasks import download_mp3
from django.contrib import messages

def index(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        email = form.cleaned_data.get('email')
        full_url = request.get_host()
        Download.objects.create(url=url, email=email)
        download_mp3.delay(url, email, full_url)
        messages.success(request, 'Your file download link has been sent to your email.')
        return render(request, 'download/index.html', {'form': form})
    return render(request, 'download/index.html', {'form': form})
