try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls import url
    patterns = list

from django.views.decorators.cache import cache_page

try:
    from oscar.core.application import OscarConfig
except ImportError:
    from django.apps import AppConfig as OscarConfig


class ShippingConfigBase(object):
    name = 'oscar_shipping'

    def get_urls(self):
        urlpatterns = super(ShippingConfigBase, self).get_urls()
        urlpatterns += patterns('',
            url(r'^city-lookup/(?P<slug>[\w-]+)/$', cache_page(60*10)(self.city_lookup_view.as_view()),
                name='city-lookup'),
        )
        urlpatterns += patterns('',
            url(r'^details/(?P<slug>[\w-]+)/$', cache_page(60*10)(self.shipping_details_view.as_view()),
                name='charge-details'),
        )
        return self.post_process_urls(urlpatterns)

    def ready(self):
        from . import views
        self.city_lookup_view = views.CityLookupView
        self.shipping_details_view = views.ShippingDetailsView


class ShippingConfig(ShippingConfigBase, OscarConfig):
    pass


try:
    from oscar.core.application import Application


    class ShippingApplication(ShippingConfigBase, Application):
        pass


    application = ShippingApplication()

except ImportError:
    pass
