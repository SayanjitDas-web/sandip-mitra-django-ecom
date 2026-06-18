from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def create_product(request):
    if request.method == "POST":
        product_title = request.POST.get("product_title")
        product_details = request.POST.get("product_details")
        product_price = request.POST.get("product_price")
        product_image = request.FILES.get("product_image")
        
        Product.objects.create(
            product_title = product_title,
            product_details = product_details,
            product_price = product_price,
            product_image = product_image
        )
        
        return redirect("product_list")
    
    return render(request,"create_product.html")

def product_list(request):
    products = Product.objects.all()
    
    return render(request,"products.html",{
        "products":products
    })
    
def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    
    return render(request,"product.html",{
        "product":product
    })