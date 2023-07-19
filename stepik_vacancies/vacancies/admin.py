from django.contrib import admin
from vacancies.models import Vacancy, Company, Speciality

# Register your models here.
admin.site.register(Company)
admin.site.register(Speciality)
admin.site.register(Vacancy)
