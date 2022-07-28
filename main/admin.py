from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'password')}),
        (('Personal info'), {'fields': ('name', )}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('date_joined', 'last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone', 'email', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    list_display = ('username', 'phone', 'email',  'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'phone', 'email')

admin.site.register(CustomUser, CustomUserAdmin)

