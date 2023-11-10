from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

# from dcim.models import Device

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_friendlyurl", {})

class FURLRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/plugins/furl/redirect/'):
            return response

        path_parts=request.path.split('/')

        if len(path_parts)>4:
            if '=' in path_parts[3]:
                redirect_url = reverse("plugins:netbox_friendlyurl:redirect",kwargs = { "match" : request.path } )
                return redirect(redirect_url)

        return response