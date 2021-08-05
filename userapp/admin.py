from django.contrib import admin

# Register your models here.

# Register your models here.
from userapp.models import APIUser

admin.site.register(APIUser)


# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm
#
# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = MyUser
#
# class MyUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#
#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields': ('some_extra_data',)}),
#     )
#
#
# admin.site.register(MyUser, MyUserAdmin)


