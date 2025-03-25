import pytest
from unittest.mock import patch
from shortener.models import Urls


@pytest.mark.django_db
class TestUrlsModel:
    @patch("shortener.models.Urls.generate_path")
    def test_save_creates_path_and_shortened_url(self, mock_generate_path):

        mock_generate_path.return_value = "abc123"

        url = Urls.objects.create()

        assert url.path == "abc123"

        assert url.shortened_url == "http://127.0.0.1:8000/abc123"

    @pytest.mark.django_db
    def test_save_does_not_generate_new_path_if_path_exists(self):

        url = Urls.objects.create(path="xyz456")

        assert url.path == "xyz456"

        assert url.shortened_url == "http://127.0.0.1:8000/xyz456"
