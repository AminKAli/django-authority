from django.contrib.auth.admin import UserAdmin
from example.users.models import User


admin.site.register(User, UserAdmin)
