from pathlib import Path 
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path('_file_').resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates') 


# Quick start development settings - unsutibale for production 
# See https://docs.djangoproject.com/en/3.2.3/howto/deployment/checklist/

#SECURITY WARNING: Keep the secret key used in production secret: 
SECRET_KEY = '83e21kif7kjn1s2=$c5i=6%+x0@1_c$54xxd^^e(u)3j_jk-(k'

#SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOST = []



#Application Definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'app_users',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.midleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contirb.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutor_made_easy.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [TEMPLATE_DIR],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'tutor_made_easy.wsgi_application'