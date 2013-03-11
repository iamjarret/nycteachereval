from django.contrib import admin
from teachers import models


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'school')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Teachers, TeacherAdmin)
admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.City)
admin.site.register(models.Borough,)
admin.site.register(models.District)
admin.site.register(models.Neighborhood)