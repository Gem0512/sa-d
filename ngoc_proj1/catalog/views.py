from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from .models import Category, Product
# Create your views here.

def catalog(request,  template_name ='catalog/category.html'):
    page_title = "Musical Instruments and Sheet Music for Musicians"
    return render(
        request,
        template_name,
        locals(),
    )
    
def product(request,  template_name ='catalog/product.html'):
    page_title = "Musical Instruments and Sheet Music for Musicians"
    return render(
        request,
        template_name,
        locals(),
    )
    
def index(request, template_name="catalog/index.html"):
    page_title = "Musical Instruments and Sheet Music for Musicians"
    return render(
        request,
        template_name,
        locals(),
    )