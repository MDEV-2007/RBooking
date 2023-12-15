from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('profile_picture',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ('profile_picture',)}),
    )

admin.site.register(User, UserAdmin)