from django.urls import re_path
from .views import RedirectView

urlpatterns = [
    re_path(r"^redirect/(?P<match>.+)/$", RedirectView, name="redirect"),
]