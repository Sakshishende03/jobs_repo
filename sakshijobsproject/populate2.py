import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sakshijobsproject.settings')
import django
django.setup()
from testapp.models import PuneJobs
from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    d1 = randint(6,9)
    num =''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project Manager','Team Leader','Software Enginner','HR','Associate Engineer'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        Hyd_jobs_record = PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, address=faddress, email=femail, phonenumber=fphonenumber)

n = int(input("Enter Number of Records: "))
populate(n)
print("{} Record(s) Inserted Successfully".format(n))
