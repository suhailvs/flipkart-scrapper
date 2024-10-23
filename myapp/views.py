from django.shortcuts import render
from django.http import HttpResponse
from myapp.parse import Parse
from myapp.models import Product
# Create your views here.
def products(request):
    qs = Product.objects.all()
    return render(request,'myapp/products.html',{'products':qs})

def parse_products(request):
    
    p = Parse(my_model=Product)
    p.run()

    return HttpResponse('success')