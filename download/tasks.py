import youtube_dl
from converter import settings
from django.core.mail import send_mail
from converter.celery import app



@app.task
def download_mp3(url, email, full_url):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    with youtube_dl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url)
        filename = info['title']

        send_mail(
            'Your converted mp3-format is read!',
            ('http://' + full_url + '/media/' + filename).replace(" ", "%20") + '.mp3',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )