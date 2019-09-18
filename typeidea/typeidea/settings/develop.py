from .base import *


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import pymysql
pymysql.install_as_MySQLdb()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': '147896325',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
