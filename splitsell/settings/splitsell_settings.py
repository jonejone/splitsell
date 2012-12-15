TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',

    'splitsell.splash',

    'django_extensions',
)


TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
ROOT_URLCONF = 'splitsell.splash.urls'
#LANGUAGE_CODE = 'nb_NO'
MEDIA_URL = '/media/'
DEBUG = False
