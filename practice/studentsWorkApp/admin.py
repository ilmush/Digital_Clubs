from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(Post)
admin.site.register(Role)
