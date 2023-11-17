from django.shortcuts import render, redirect
from .forms import NewOrderForm

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
