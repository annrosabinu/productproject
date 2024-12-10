from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def productform(request):
    return render(request, 'Productform.html')

def productregister(request):
    if request.method == 'POST':
        p_name = request.POST.get('pname')
        p_desc=request.POST.get('pdesc')
        p_qty=request.POST.get('qty')
        p_amt=request.POST.get('amt')
        pobj=Product(productname=p_name, productdescription=p_desc,productquantity=p_qty,productprice=p_amt)
        pobj.save()
        return redirect('productdetails')


def productdetails(request):
    products=Product.objects.all()
    return render(request, 'productdetails.html',{'products':products})

def editdetails(request,id):
    pobj=Product.objects.get(id=id)
    return render(request, 'edit.html',{'p':pobj})

def editpage(request,id):
    if request.method == 'POST':
        product=Product.objects.get(id=id)
        product.productname=request.POST.get('pname')
        product.productdescription=request.POST.get('pdesc')
        product.productquantity=request.POST.get('qty')
        product.productprice=request.POST.get('amt')
        product.save()
        return redirect('productdetails')
    return render(request,'edit.html')

def delete(request,id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('productdetails')
    