try:
    import oscar.apps.shipping.apps as apps

    default_app_config = 'test_project.shipping.apps.ShippingConfig'
except ImportError:
    pass
