from django.contrib import admin
from teachers import models


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'dbn')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Teachers, TeacherAdmin)
admin.site.register(models.School, SchoolAdmin)