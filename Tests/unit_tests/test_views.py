"""
This file demonstrates writing tests using the unittest module.
"""

import django
from django.test import TestCase
import os
import sys

"""
When we use Django, we have to tell it which settings we are using. We do this by using an environment variable, DJANGO_SETTINGS_MODULE. 
This is set in manage.py. We need to explicitly set it for tests to work with pytest.
"""

sys.path.append(os.path.join(os.getcwd(), 'Application'))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "python_webapp_django.settings"
)
django.setup()

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()

    def test_unit_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'SELab 關心您的身體健康', 1, 200, html=True)

    def test_unit_normal(self):
        """Tests the home page."""
        response = self.client.post('/', {'height':1.7,'weight':"60"})
        self.assertContains(response, '20.76', 1, 200, html=True)
    
