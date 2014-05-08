ALLOWED_HOSTS = ['192.168.43.100:8091']
DEBUG = True 
EMAIL_HOST = 'localhost' 
EMAIL_PORT = '1025' 
EMAIL_HOST_USER = '' 
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = '' 
DB_PASS = ''
DB_HOST = '/var/run/postgresql/'
# Configuracoes para rodar com WSGI em Virtualhosts no Apache
#MEDIA_URL = 'http://192.168.0.1/gallery/media/'
#ADMIN_MEDIA_PREFIX = '/gallery/admin_media/'
#SESSION_COOKIE_PATH = '/amontoado_3'
LOGIN_REDIRECT_URL = '/amontoado_3/flat/fb_app/instrucoes/'
LOGIN_URL = '/amontoado_3/accounts/login/'
LOGOUT_URL = '/amontoado_3/accounts/logout/'
MEDIA_ROOT = '/home/making_software/projetos/making_software_made/amontoado//amontoado_3/media/'
MEDIA_URL = '/amontoado_3/media/'
URL_ROOT = '/amontoado_3/'
ADMINS = ()
# allauth
# Nao estah logando com e-mail soh com username
ACCOUNT_AUTHENTICATION_METHOD = ("username")
#ACCOUNT_EMAIL_VERIFICATION = ("mandatory")
SOCIALACCOUNT_EMAIL_VERIFICATION = ("none")
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
SOCIALACCOUNT_AUTO_SIGNUP =True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amontoado_3',             
        'USER': 'postgres',             
        'PASSWORD': DB_PASS,                 
        # isso eh muito importante, eh onde estah o socket do postgres instalado por default
        # O psycopg2 expects Postgres socket to be in /var/run/postgresql/
        #http://stackoverflow.com/questions/5500332/cant-connect-the-postgresql-with-psycopg2
        'HOST': DB_HOST,                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                     # Set to empty string for default. Not used with sqlite3.
    }
}
STATIC_URL = '/static_files/making_software/'
STATICFILES_DIRS = (
    '//home/making_software/projetos/making_software_made/amontoado//amontoado_3/static_files',
)
SECRET_KEY = 'uvg1$c^9ey*097s(^ylf)-ffil#q-j#o1=ng!wf%vlk3m_3i)h'
ROOT_URLCONF = 'amontoado_3.urls'
WSGI_APPLICATION = 'amontoado_3.wsgi.application'
TEMPLATE_DIRS = (
    '/home/making_software/projetos/making_software_made/amontoado//amontoado_3/templates/'
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django_admin_bootstrapped', # Precisa estar antes do django.contrib.admin
    'django.contrib.admin',
    #'django.contrib.admindocs',
    #'fb_iframe', # Para nao dar pau de CSRF no FB
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'wysiwyg_forms',
    'bsct',
    'guardian',
    'south',
        'itens_4',
        'projeto_3',
)
# Para utilizar o Django Guardian
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)
# Para utilizar o Django Guardian
ANONYMOUS_USER_ID = -1
GUARDIAN_RAISE_403 = True
# Nao sei bem como funciona isso.
# Talvez seja melhor pegar do original
SITE_ID = 1
# Essas propriedades nao mudam
MANAGERS = ADMINS
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = ''
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
ACCOUNT_ACTIVATION_DAYS = 7
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'fb_iframe.middleware.FacebookMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount'
)
"""
LOGGING = {
    'version': 1,
    #'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'logs/mylog.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'INFO',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': 'logs/django_request.log',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
"""
