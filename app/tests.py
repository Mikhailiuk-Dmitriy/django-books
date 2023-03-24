from django.test import TestCase

from .models import Author


class BaseTestCase(TestCase):
    def test_base(self):
        author = Author.objects.create(
            first_name="Эдуард", last_name="Успенский"
        )
        authors = Author.objects.all()
        assert author in authors
