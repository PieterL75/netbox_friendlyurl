from extras.plugins import PluginConfig

from .middleware import FURLRedirectMiddleware

class NetBoxFriendlyURLConfig(PluginConfig):
    name = 'netbox_friendlyurl'
    verbose_name = ' NetBox User Friendly URLs'
    description = 'Create urls in NetBox that are more user friendly and that redirect to real netbox urls'
    version = '0.1'
    base_url = 'furl'
    middleware = ["netbox_friendlyurl.middleware.FURLRedirectMiddleware"]

config = NetBoxFriendlyURLConfig

