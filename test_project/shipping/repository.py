from oscar.apps.shipping import repository

from .methods import *
from . import models


class Repository(repository.Repository):

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        methods = [SelfPickup(),]
        #...
        methods.extend(list(models.ShippingCompany.objects.all().filter(is_active=True)))
        return methods
