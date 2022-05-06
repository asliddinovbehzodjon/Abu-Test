from django.shortcuts import render
from .models import Course
# Create your views here.
def home(request):
     kurslar = Course.objects.all()
     print(f"######{kurslar} #################")
     return render(request,'index.html',{'kurslar': kurslar})