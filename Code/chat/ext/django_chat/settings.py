"""
Default Chat settings for Django.
"""
from django.conf import settings
from chat import constants


CHAT = getattr(settings, 'CHAT', {})

CHAT_DEFAULTS = {
    'name': 'Chat',
    'storage_adapter': 'chat.storage.DjangoStorageAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

CHAT = CHAT_DEFAULTS.copy()
CHAT.update(CHAT_SETTINGS)
