from django.db import models
import string, random

class Urls(models.Model):
    path = models.CharField(max_length=8, unique=True, editable=False)
    redirect_to = models.URLField()
    shortened_url = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.generate_path()
        self.shortened_url = f"http://127.0.0.1:8000/{self.path}"
        super().save(*args, **kwargs)

    def generate_path(self):
        while True:
            path = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if not Urls.objects.filter(path=path).exists():
                return path

# Create your models here.
