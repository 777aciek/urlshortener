import pytest
from shortener.models import Urls

# from django.contrib.auth.models import Urls


@pytest.fixture
def clear_urls(db):
    Urls.objects.all().delete()


@pytest.mark.django_db
def test_generate_path_length(clear_urls):
    instance = Urls()

    path = instance.generate_path()

    assert len(path) == 8
