from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student, Mentor, FinalMentor
from django.contrib.auth.models import User
# import auth.PersonAdmin


@admin.register(Student)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Mentor)
class PersonAdmin(ImportExportModelAdmin):
    pass
# @admin.register(User)
# class PersonAdmin(ImportExportModelAdmin):
#     pass






# admin.site.register(Student)
# admin.site.register(Mentor)
admin.site.register(FinalMentor)