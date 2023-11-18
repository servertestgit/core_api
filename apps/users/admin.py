from django.contrib import admin
from django.conf import settings
from .models import User, Code

admin.site.register([User, Code,])
