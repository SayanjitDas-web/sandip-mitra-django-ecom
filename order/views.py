from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        shipping_address = request.POST.get("shipping_address")
        phone_number = request.POST.get("phone_number")
        
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            phone_number=phone_number,
        )
        
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.product_price
        )
        
        return redirect("order_detail", order.id)
    
    return render(request, "create_order.html", {
        "product": product
    })
    
@login_required
def order_detail(request, id):
        order = get_object_or_404(
            Order,
            id=id,
            user=request.user
        )

        return render(request, "order_detail.html", {
            "order": order
        })
        
        
@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "my_orders.html", {
        "orders": orders
    })
    

@login_required
def cancel_order(request, id):
    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    if order.status == "pending":
        order.status = "cancelled"
        order.save()

    return redirect("order_detail", order.id)