from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DownloadForm
from .models import Download
import youtube_dl
from django.core.mail import send_mail

def index(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        email = form.cleaned_data.get('email')
        Download.objects.create(url=url, email=email)
        options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])

            send_mail(
               'Received', 'you received message', [email], fail_silently=False
            )
    return render(request, 'download/index.html', {'form': form})
