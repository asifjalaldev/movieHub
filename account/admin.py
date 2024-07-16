from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
# Register your models here.
# class CustomUserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         obj.extra_data='extra data send from save_model'
#         obj.save()

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)