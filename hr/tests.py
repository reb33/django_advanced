# from django.test import TransactionTestCase, Client
# from django.db.models import Count
#
# from hr.models import Department
#
#
# class DepartmentTests(TransactionTestCase):
#
#     def test(self):
#         d = Department.objects.all()
#         print(d)


import os

import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')

    # Initialize Django
    django.setup()

    from hr.models import Department

    d = Department.objects.aggregate()

    print(d)
