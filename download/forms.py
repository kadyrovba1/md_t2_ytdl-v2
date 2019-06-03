from django import forms
from .models import Download

class DownloadForm(forms.ModelForm):
    email = forms.EmailField()
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    class Meta:
        model = Download
        fields = ('url',)