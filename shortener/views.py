from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Urls
from .forms import UrlsForm
import logging

logger = logging.getLogger(__name__)


@login_required
def r_redirect(request, path):
    redirect_obj = get_object_or_404(Urls, path=path)
    return redirect(redirect_obj.redirect_to)


@login_required
def add_url(request):
    if request.method == "POST":
        form = UrlsForm(request.POST)
        if form.is_valid():

            redirect_to = form.cleaned_data["redirect_to"]

            existing_url = Urls.objects.filter(redirect_to=redirect_to).first()

            if existing_url:

                new_shortened_url = existing_url.shortened_url
                logger.warning(
                    f"URL with redirect {redirect_to} already exists. Skipping save."
                )
            else:

                new_url = form.save()
                new_shortened_url = new_url.shortened_url

            return render(
                request,
                "urls.html",
                {
                    "form": form,
                    "urls": Urls.objects.all(),
                    "new_shortened_url": new_shortened_url,
                },
            )

    else:
        form = UrlsForm()

    urls = Urls.objects.all()
    return render(request, "urls.html", {"form": form, "urls": urls})
