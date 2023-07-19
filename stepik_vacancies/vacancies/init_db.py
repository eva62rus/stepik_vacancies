from vacancies.models import Vacancy, Speciality, Company
from vacancies.data import *
import os



SPECIALITY_PICTURES = {
    "frontend": "specty_frontend.png",
    "backend": "specty_backend.png",
    "gamedev": "specty_gamedev.png",
    "devops": "specty_devops.png",
    "design": "specty_design.png",
    "products": "specty_products.png",
    "management": "specty_management.png",
    "testing": "specty_testing.png",
}


def init_companies():
    for company in companies:
        comp = Company.objects.create(
            id=company["id"],
            name=company["title"],
            location=company["location"],
            logo=os.path.join("/img/static/", company["logo"]),
            description=company["description"],
            employee_count=company["employee_count"],
        )
        comp.save()


def init_specialties():
    for specialty in specialties:
        spec = Speciality.objects.create(
            code=specialty["code"],
            title=specialty["title"],
            picture=os.path.join(
                "/img/specialties/", SPECIALITY_PICTURES[specialty["code"]]
            ),
        )
        spec.save()


def init_vacancies():
    for job in jobs:
        vacany = Vacancy.objects.create(
            id=job["id"],
            title=job["title"],
            speciality=Speciality.objects.get(code=job["specialty"]),
            company=Company.objects.get(id=job["company"]),
            skills=job["skills"],
            description=job["description"],
            salary_min=job["salary_from"],
            salary_max=job["salary_to"],
            published_at=job["posted"],
        )
        vacany.save()


def main():
    pass


if __name__ == "__main__":
    main()
