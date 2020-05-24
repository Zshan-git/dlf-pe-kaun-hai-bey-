from django.shortcuts import render, get_object_or_404, redirect
from .models import Orders
from .forms import Ordersform
# Create your views here.

def list_forms(request, *args, **kwargs): 
    form = Ordersform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    return render(request, "orders_form.html",context)

def delete_orders(request, order_id):
    obj = get_object_or_404(Orders, id = order_id)
    context = {
        "object": obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect('../../') 
    return render(request, "delete_confirm.html", context)


def list_the_orders(request):
    queryset = Orders.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "list_all.html", context)

# def list_orders(request, *args, **kwargs): 
#     obj = Orders.objects.get(id = 1)
#     context = {
#         'item': obj.Item,
#         'quantity': obj.quantity,
#         'price': obj.price,
#         'Accepted':obj.Accepted
#     }
#     return render(request, "orders.html",context)