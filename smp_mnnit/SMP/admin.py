from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student, Mentor, FinalMentor



@admin.register(Student)
class PersonAdmin(ImportExportModelAdmin):
    pass








# admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(FinalMentor)