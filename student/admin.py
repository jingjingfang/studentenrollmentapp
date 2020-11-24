from django.contrib import admin
from student.models import Studentdetails
from student.models import Coursedetails
from student.models import Enrollment


admin.site.register(Studentdetails)
admin.site.register(Coursedetails)
admin.site.register(Enrollment)

# Register your models here.
