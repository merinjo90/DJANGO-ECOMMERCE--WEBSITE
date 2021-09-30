from django.shortcuts import render
from .models import Category,Brand

# Create your views here.
#Home
def home(request):
    return render(request,'index.html')

#Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})


#Brand
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request,'brand_list.html',{'data':data})


