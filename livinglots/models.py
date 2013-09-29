from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model as django_get_model


def get_model(name):
    try:
        m = settings.LIVING_LOTS['MODELS'][name]
        return django_get_model(*m.split('.'))
    except Exception:
        raise ImproperlyConfigured(('Could not find a %s model. Did you set '
                                    'LIVING_LOTS.MODELS.%s in your '
                                    'settings.py?') % (name, name))


def get_lot_model():
    return get_model('lot')


def get_lotgroup_model():
    return get_model('lotgroup')


def get_owner_model():
    return get_model('owner')


def get_parcel_model():
    return get_model('parcel')
