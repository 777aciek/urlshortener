from django import forms
from .models import Urls


class UrlsForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ["redirect_to"]
