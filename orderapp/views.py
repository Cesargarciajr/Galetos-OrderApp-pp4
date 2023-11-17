from django.shortcuts import render, redirect
from .forms import NewOrderForm, ContactForm

# Rendering home page


def home(request):
    return render(request, 'index.html')


# Rendering New order page
def new_order(request):
    if request.method == "GET":
        form = NewOrderForm()
        return render(request, 'new_order.html', {'form': form})
    else:
        form = NewOrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/orderslist/')


# Rendering Order List page
def orders_list(request):
    return render(request, 'orders_list.html')


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
