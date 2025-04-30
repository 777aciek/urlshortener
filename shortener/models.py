from django.db import models
from django.conf import settings
import string, random, logging

logger = logging.getLogger(__name__)


class Urls(models.Model):
    path = models.CharField(max_length=8, unique=True, editable=False)
    redirect_to = models.URLField()
    shortened_url = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.generate_path()
            logger.debug(f"Generated path: {self.path}")

        self.shortened_url = f"{settings.URL_ADDRESS}{self.path}"
        logger.debug(f"Generated shortened URL: {self.shortened_url}")

        if not Urls.objects.filter(redirect_to=self.redirect_to).exists():
            logger.info(
                f"Saving new URL: {self.shortened_url} redirecting to {self.redirect_to}"
            )
            super().save(*args, **kwargs)

    def generate_path(self):
        logger.debug("Starting path generation...")
        while True:
            path = "".join(random.choices(string.ascii_letters + string.digits, k=8))
            if not Urls.objects.filter(path=path).exists():
                logger.debug(f"Unique path generated: {path}")
                return path


# Create your models here.
