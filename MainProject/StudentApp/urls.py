from django.urls import path
from .import views
urlpatterns = [
	path('',views.home,name="hm"),
	path('listofstudents/',views.allstdntdetails,name="alstdnt"),
	path('pdf_view/',views.preview_pdf,name="prvw_pdf"),
	path('pdf_download/',views.downld_pdf,name="dwn_pdf"),
]