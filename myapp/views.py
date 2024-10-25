from django.shortcuts import render
from django.http import HttpResponse
from myapp.parse import Parse,Parse2
from myapp.models import Product
from pathlib import Path
from django.core.paginator import Paginator
from django.db.models import Count
# Create your views here.
def products(request):
    qs = Product.objects.all()
    q = request.GET.get("q")
    star = request.GET.get("star")
    c = request.GET.get('category')
    if q: qs = qs.filter(title__icontains=q)    
    if star: 
        if star == '4p':
            qs = qs.filter(star__in=[f'4.{i}' for i in range(1,10)])
        else:
            qs = qs.filter(star=star)
    if c: qs = qs.filter(category=c)
    
    paginator = Paginator(qs, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")    
    page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/products.html', {
        "page_obj": page_obj,
        "categories":qs.values('category').annotate(c=Count('id')),
        "stars":qs.values('star').annotate(c=Count('id')),
    })



def parse_products(request,f):
    if f == 1:
        dname='htmlfiles'
    elif f == 2:
        dname='htmlfiles2'
    else:
        return HttpResponse('must be 1 or 2')
    directory = Path(dname)
    files = [f.name for f in directory.iterdir() if f.is_file()]
    for fname in files:
        if f == 1:
            p = Parse(fname=f'{dname}/{fname}',my_model=Product)
        else:
            p = Parse2(fname=f'{dname}/{fname}',my_model=Product)
        p.run()
    return HttpResponse('success')