from django.shortcuts import render
from django.http import HttpResponse 
from student.models import Studentdetails
from student.models import Coursedetails
from student.models import Enrollment
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Count


# Create your views here.


@login_required
def home(request):    
 	 
    numofstudent=Studentdetails.objects.all().count()     
    avggpa =list(Studentdetails.objects.all().aggregate(Avg('gpa')).values())[0]
    numofsenior=Studentdetails.objects.all().filter(year='Senior').count()
    numofjunior=Studentdetails.objects.all().filter(year='Junior').count()	
    numoffreshmen=Studentdetails.objects.all().filter(year='Freshmen').count()
    numofcourse=Coursedetails.objects.all().count()  
    context = {'numofstudent':numofstudent,'avggpa': avggpa,'numofsenior': numofsenior, 'numofjunior': numofjunior,'numoffreshmen': numoffreshmen,'numofcourse':numofcourse} 
    return render(request, 'student/home.html', context)  


 
def dictfetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    columns = [col[0] for col in cursor.description]
    return [
       dict(zip (columns, row)) 
       for row in cursor.fetchall()
]



@login_required
def coursedetails(request):
    course = Coursedetails.objects.all()
    paginator = Paginator(course,10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
    return render(request, 'student/coursedetails.html',{'data':coursedata})
   



@login_required
def studentdetails(request):
    student = Studentdetails.objects.all()
    paginator = Paginator(student,10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)
    return render(request, 'student/studentdetails.html',{'data':studentdata})



@login_required
def enrollment(request):
    student = Studentdetails.objects.all()
    enrollmentdata =Enrollment.objects.all()
    course = Coursedetails.objects.all()
    enrollment =''
    
    
    if('firstname' in request.session):
       enrollmentdata =Enrollment.objects.filter(firstname=request.session['firstname'])
    if('fname' in request.GET and 'coursename' not in request.GET):
        fname=request.GET.get('fname')
        request.session['firstname']=fname           
        return HttpResponse('Success')         
        

    if('fname' in request.GET and 'coursename' in request.GET):
        fname=request.GET.get('fname')
        coursename=request.GET.get('coursename')
        enrollmentddata=Enrollment.objects.filter(firstname=fname)
        for row in enrollmentdata:
                if row.course==coursename:
                   return HttpResponse('Error')     
                                 
        newdata = Enrollment(firstname=fname, course=coursename)
        newdata.save()
        return HttpResponse('Success')
   
    return render(request, 'student/enrollment.html', {'student':student,'course':course, 'enrollment':enrollmentdata})


