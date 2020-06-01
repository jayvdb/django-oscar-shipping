try:
    import oscar.apps.shipping.apps as apps


    class ShippingConfig(apps.ShippingConfig):
        name = 'test_project.shipping'
        label = 'shipping'
except ImportError:
    from oscar.core.application import Application


    class ShippingApplication(Application):
        name = 'shipping'


    application = ShippingApplication()
