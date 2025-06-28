from django.db import models

# Create your models here.
class Staff_base(models.Model):
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)

    def get_role():
        return "staffbase parent"


class Manager(Staff_base):
    department=models.CharField(max_length=200)
    has_company_card=models.BooleanField(default=True)

    def get_role():
        return "Manager"

class Intern(Staff_base):
    mentor=models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end=models.DateField()

    def get_role():
        return "Intern"
