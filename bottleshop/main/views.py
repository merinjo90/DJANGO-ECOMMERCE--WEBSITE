from django.shortcuts import render
from .models import Category,Brand,Product

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

#Product list
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')

    return render(request,'product_list.html',
        {
            'data':data,
            'cats':cats,
            'brands':brands,
        })


