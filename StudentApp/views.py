from django.shortcuts import render,redirect
from .forms import StdntForm
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
import pdfkit
from django.contrib import messages

# Create your views here.

def home(request):
	p = Student.objects.all()
	k = p.count()
	paginator = Paginator(p, 8)
	page_number = request.GET.get('page')
	pg_obj = paginator.get_page(page_number)
	return render(request,'home.html',{'st':pg_obj,'cnt':k})

def allstdntdetails(request):
	t = Student.objects.all()
	pp = t.count()
	q = ''
	search_result_count = None
	swal_message = None
	swal_icon = None
	if request.method == "POST":
		if "add" in request.POST:
			k = StdntForm(request.POST,request.FILES)
			if k.is_valid():
				k.save()
				messages.success(request, "Student added successfully!")
				return redirect("/listofstudents")
		elif "update" in request.POST:
			mp = Student.objects.get(id=request.POST['id'])
			k = StdntForm(request.POST,request.FILES,instance=mp)
			if k.is_valid():
				k.save()
				messages.success(request, "Student updated successfully!")
				return redirect('/listofstudents')
		elif "delete" in request.POST:
			km = Student.objects.get(id=request.POST['id'])
			km.delete()
			messages.success(request, "Student deleted successfully!")
			return redirect('/listofstudents')
		elif "search" in request.POST:
			q = request.POST['searchquery']
			if q == "":
				swal_message = f'No records found for "{q}"'
				swal_icon = "error"
			else:
				t = Student.objects.filter(Q(fname__icontains=q)|Q(lname__icontains=q)|Q(email__icontains=q)|Q(mobile__icontains=q))
				search_result_count = t.count()
				if search_result_count == 0:
					swal_message = f'No records found for "{q}"'
					swal_icon = "warning"
				else:
					swal_message = f'{search_result_count} record(s) found for "{q}"'
					swal_icon = "success"
		else:
			return redirect('/listofstudents')

	paginator = Paginator(t, 5)
	page_number = request.GET.get('page')
	pg_obj = paginator.get_page(page_number)
	for s in pg_obj:
		s.ep = StdntForm(instance=s)
	gg = StdntForm()
	return render(request,'allstudents.html',{'g':gg,'y':pg_obj,'q':q,'swal_message': swal_message,
        'swal_icon': swal_icon,"cc":pp})


def preview_pdf(request):
    students = Student.objects.all()
    html_string = render_to_string('students_pdf.html', {'students': students})
    pdf = pdfkit.from_string(html_string, False, configuration=settings.PDFKIT_CONFIG,
        options={"enable-local-file-access": ""})
    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'inline; filename="students.pdf"'
    return response

def downld_pdf(request):
    students = Student.objects.all()
    html_string = render_to_string('students_pdf.html', {'students': students})
    pdf = pdfkit.from_string(html_string, False, configuration=settings.PDFKIT_CONFIG,
        options={"enable-local-file-access": ""})
    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'
    return response

   