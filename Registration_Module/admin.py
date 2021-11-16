from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import *

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.utils.translation import ugettext_lazy as _

from Registration_Module.models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_hospital_staff', 'is_normal_user',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            # (_('user_info'), {'fields': ('native_name', 'phone_no')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_hospital_staff']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(HospitalStaff)