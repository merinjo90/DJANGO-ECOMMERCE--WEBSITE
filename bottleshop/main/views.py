from django.shortcuts import render

# Create your views here.
#Home
def home(request):
    return render(request,'index.html')

#Category
def category_list(request):
    return render(request,'category_list.html')



