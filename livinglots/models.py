from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_model_name(name, optional=True):
    try:
        return settings.LIVING_LOTS['MODELS'][name]
    except KeyError:
        if not optional:
            raise ImproperlyConfigured(('Could not find a %s model. Did you '
                                        'set LIVING_LOTS.MODELS.%s in your '
                                        'settings.py?') % (name, name))
        return None


def get_model(name, optional=True):
    try:
        model_name = get_model_name(name, optional=optional)
        return apps.get_model(*model_name.split('.'))
    except Exception:
        if not optional:
            raise ImproperlyConfigured(('Could not find a %s model. Did you '
                                        'set LIVING_LOTS.MODELS.%s in your '
                                        'settings.py?') % (name, name))
        return None


def get_lot_model():
    return get_model('lot')


def get_lot_model_name():
    return get_model_name('lot')


def get_lotgroup_model():
    return get_model('lotgroup')


def get_lotlayer_model():
    return get_model('lotlayer', optional=True)


def get_organizer_model():
    return get_model('organizer')


def get_organizer_model_name():
    return get_model_name('organizer')


def get_owner_model():
    return get_model('owner')


def get_owner_model_name():
    return get_model_name('owner')


def get_owner_contact_model():
    return get_model('owner_contact')


def get_owner_contact_model_name():
    return get_model_name('owner_contact')


def get_owner_group_model():
    return get_model('owner_group')


def get_owner_group_model_name():
    return get_model_name('owner_group')


def get_parcel_model():
    return get_model('parcel')


def get_parcel_model_name():
    return get_model_name('parcel')


def get_pathway_model():
    return get_model('pathway')


def get_stewardproject_model():
    return get_model('stewardproject')


def get_stewardproject_model_name():
    return get_model_name('stewardproject')
