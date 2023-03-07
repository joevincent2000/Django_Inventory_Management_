from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def display_product(request):
    items = Product.objects.all()
    context = {
           'items' :items,
           'header' : 'Product',
    }
    return render(request, 'product.html',context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request,'add_product.html',{'form':form})

def edit_product(request,pk):
    item = get_object_or_404(Product,product_id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance = item)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance = item)
    return render(request,'edit_product.html',{'form':form,'item':item})
    
def delete_product(request,pk):

    Product.objects.filter(product_id=pk).delete()

    items = Product.objects.all()

    context = {
        'items':items
    }
    return render(request, 'index.html',context)


#Location

def display_location(request):
    items = Location.objects.all()
    context = {
           'items' :items,
           'header' : 'Location',
    }
    return render(request, 'location.html',context)

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_location')
    else:
        form =LocationForm()
    return render(request,'add_location.html',{'form':form})

def edit_location(request,pk):
    item = get_object_or_404(Location,location_id=pk)

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_location')
    else:
        form = LocationForm(instance=item)
    return render(request, 'edit_location.html', {'form': form})

    
def delete_location(request,pk):

    Location.objects.filter(location_id=pk).delete()

    items = Location.objects.all()

    context = {
        'items':items
    }
    return render(request, 'location.html',context)

def product_movement(request):
    items = ProductMovement.objects.all()
    context = {
           'items' :items,
           'header' : 'ProductMovement',
    }
    return render(request, 'product_movement.html',context)

def add_product_movement(request):
    if request.method == 'POST':
        form = ProductMovementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_movement')
    else:
        form =ProductMovementForm()
    return render(request,'add_product_movement.html',{'form':form})

def edit_product_movement(request,pk):
    item = get_object_or_404(ProductMovement,movement_id=pk)

    if request.method == 'POST':
        form = ProductMovementForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product_movement')
    else:
        form = ProductMovementForm(instance=item)
    return render(request, 'edit_product_movement.html', {'form': form})


def product_balance(request):
    products = Product.objects.all()
    balance = []
    for product in products:
        total_in = ProductMovement.objects.filter(product=product, to_location__isnull=False).aggregate(Sum('qty'))['qty__sum'] or 0
        total_out = ProductMovement.objects.filter(product=product, from_location__isnull=False).aggregate(Sum('qty'))['qty__sum'] or 0
        balance.append({
            'product': product,
            'total_in': total_in,
            'total_out': total_out,
            'quantity': total_in - total_out
        })
    context = {
        'items' : balance,
        'header' : 'Product Balance',
    }
    return render(request, 'product_balance.html', context)
