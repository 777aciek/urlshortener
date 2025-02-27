from django.shortcuts import render, redirect, get_object_or_404
from .models import Urls
from .forms import UrlsForm

# Create your views here.
def r_redirect(request, path):
    redirect_obj = get_object_or_404(Urls, path=path)
    return redirect(redirect_obj.redirect_to)

def add_url(request):
    if request.method == 'POST':
        form = UrlsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_url')

    else:
        form = UrlsForm()

    urls = Urls.objects.all()
    return render(request, 'urls.html', {'form': form, 'urls': urls})