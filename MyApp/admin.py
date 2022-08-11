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


class StripeSubscriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'start_date', 'status')
    list_filter = ('status',)
    search_fields = ('start_date', 'status',)
    ordering = ('id', )


admin.site.register(StripeSubscription, StripeSubscriptionAdmin)


class MyStripeModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'stripe_subscription')
    list_filter = ('phone_number',)
    search_fields = ('name', 'phone_number',)
    ordering = ('id', )


admin.site.register(MyStripeModel, MyStripeModelAdmin)


class CustomUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'customer', 'subscription')
    search_fields = ('customer',)
    ordering = ('id', )


admin.site.register(CustomUser, CustomUserAdmin)


class MembershipAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'customer')
    list_filter = ('user', 'customer',)
    search_fields = ('user', 'customer')
    ordering = ('id', )


admin.site.register(Membership, MembershipAdmin)





################### Changing Admin Header ########################################

admin.site.site_header = "Track Enterprise Customers"
admin.site.index_title = " Track Enterprise Customers Administration Panel"
admin.site.site_title = "Track Enterprise Customers"

