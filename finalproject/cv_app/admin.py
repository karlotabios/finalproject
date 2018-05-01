from django.contrib import admin

from cv_app.models import Person, WorkExperience, Education, Interest

# Register your models here.

admin.site.register(Person)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Interest)

