from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login','date_joined','is_admin','is_staff','is_active','is_superadmin')
    list_display_links= ('email', 'first_name', 'last_name')
    readonly_fields= ('last_login','date_joined')
    ordering= ('-date_joined',)
    list_per_page= 20
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.profile_picture:
            return format_html('<img src="{}" width="38" height="38" style="border-radius:50%;object-fit:cover;border:1px solid #e5e7eb;">', object.profile_picture.url)
        initials = (object.user.first_name[:1] or object.user.email[:1] or '?').upper()
        return format_html('<span style="display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:#f1ab86;color:#111827;font-weight:700;">{}</span>', initials)

    thumbnail.short_description = 'Profile Picture'
    list_display= ('thumbnail','user','city','state','country')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'city', 'country')
    list_per_page= 20


admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
