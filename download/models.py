from django.db import models

# Create your models here.
class Download(models.Model):
    email = models.EmailField()
    url = models.URLField()
    download_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.email