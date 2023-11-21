from django.shortcuts import render, redirect
from .forms import NewOrderForm, ContactForm
from .models import NewOrderModel

# Rendering home page
def home(request):
    return render(request, 'index.html')


# Rendering New order page
def new_order(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NewOrderForm()
        else:
            order = NewOrderModel.objects.get(pk=id)
            form = NewOrderForm(instance=order)
        return render(request, 'new_order.html', {'form': form})
    else:
        if id == 0:
            form = NewOrderForm(request.POST)
        else:
            order = NewOrderModel.objects.get(pk=id)
            form = NewOrderForm(request.POST,instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            return redirect('/orderslist/')
        return render(request, 'new_order.html', {'form': form})


# Rendering Order List page
def orders_list(request):
    context = {'orders_list':NewOrderModel.objects.filter(author=request.user)}
    return render(request, 'orders_list.html', context)


# Delete Order
def delete_order(request, id):
    order = NewOrderModel.objects.get(pk=id)
    order.delete()
    return redirect('/orderslist/')

# Rendering Contact us page
def contact(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')


# Rendering About Us page
def about(request):
    return render(request, 'about.html')
