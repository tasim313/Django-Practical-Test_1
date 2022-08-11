from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'joining_date', 'is_active')
    list_filter = ('email',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'joining_date', 'is_active')
    date_hierarchy = 'joining_date'
    ordering = ('id', )


admin.site.register(User, UserAdmin)






################### Changing Admin Header ########################################

admin.site.site_header = "Track Enterprise Customers"
admin.site.index_title = " Track Enterprise Customers Administration Panel"
admin.site.site_title = "Track Enterprise Customers"

