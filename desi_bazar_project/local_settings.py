SECRET_KEY = ''

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}
STRIPE_TEST_PUBLISHABLE_KEY = ''
STRIPE_TEST_SECRET_KEY = ''

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST =
# EMAIL_HOST_USER =
# EMAIL_HOST_PASSWORD =
# EMAIL_PORT =
# EMAIL_USE_SSL =
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
