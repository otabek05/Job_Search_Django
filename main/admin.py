from django.contrib import admin

from . import models



admin.site.register(models.Job)
admin.site.register(models.Category)
admin.site.register(models.Education)
admin.site.register(models.Location)
admin.site.register(models.Salary)