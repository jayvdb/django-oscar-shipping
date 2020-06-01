import os.path
import sys

try:
    from django.conf import settings
    from django.urls import reverse_lazy

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="oscar_shipping.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "oscar.apps.address",
            "oscar.apps.catalogue",
            "oscar.apps.catalogue.reviews",
            "oscar.apps.customer",
            'oscar.apps.search',
            'oscar.apps.voucher',
            'oscar.apps.payment',
            "oscar.apps.basket",
            "oscar.apps.partner",
            "oscar.apps.order",
            "oscar.apps.offer",
            "oscar.apps.checkout",
            "oscar_shipping",
            "test_project.shipping",
            "oscar.apps.wishlists",
            # Oscar dependencies
            "widget_tweaks",
            "haystack",
            "treebeard",
            "sorl.thumbnail",
            "django_tables2",
        ],
        OSCAR_DYNAMIC_CLASS_LOADER='oscar.core.loading.default_class_loader',
        OSCAR_SLUG_FUNCTION = 'oscar.core.utils.default_slugifier',
        OSCAR_SLUG_MAP = {},
        OSCAR_SLUG_BLACKLIST = [],
        OSCAR_HOMEPAGE = reverse_lazy('catalogue:index'),
        OSCAR_IMAGE_FOLDER = 'images/products/%Y/%m/',
        OSCAR_SLUG_ALLOW_UNICODE = False,
        OSCAR_DELETE_IMAGE_FILES = True,
        OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country'),
        OSCAR_SEARCH_FACETS={'queries':{},'fields':{}},
        OSCAR_OFFERS_PER_PAGE = 20,
        OSCAR_PRODUCTS_PER_PAGE = 20,
        OSCAR_REVIEWS_PER_PAGE = 20,
        OSCAR_NOTIFICATIONS_PER_PAGE = 20,
        OSCAR_EMAILS_PER_PAGE = 20,
        OSCAR_ORDERS_PER_PAGE = 20,
        OSCAR_ADDRESSES_PER_PAGE = 20,
        OSCAR_STOCK_ALERTS_PER_PAGE = 20,
        OSCAR_DASHBOARD_ITEMS_PER_PAGE = 20,
        OSCAR_EAGER_ALERTS = False,
        OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:profile-view',
        OSCAR_HIDDEN_FEATURES= [],
        HAYSTACK_CONNECTIONS = {
            'default': {
                 'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
            },
        },
        SITE_ID=1,
        NOSE_ARGS=['-s'],
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
