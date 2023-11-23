from django.shortcuts import render, redirect
from .forms import NewOrderForm, ContactForm
from .models import NewOrderModel


# Rendering home page
def home(request):
    return render(request, 'index.html')


# Rendering New order page posting and retrieving data from database
def new_order(request, id=0):
    # if the methode is GET and id as 0 it will render tem form for New Order
    if request.method == "GET":
        if id == 0:
            form = NewOrderForm()
        else:
            # if the id is not 0 it will retrieve data from database and fill the form
            order = NewOrderModel.objects.get(pk=id)
            form = NewOrderForm(instance=order)
        return render(request, 'new_order.html', {'form': form})
    else:
        # if the method is POST then it will check the id value and post the form
        if id == 0:
            form = NewOrderForm(request.POST)
        else:
            order = NewOrderModel.objects.get(pk=id)
            form = NewOrderForm(request.POST, instance=order)
        # checks if the form is valid and save to database
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            return redirect('/orderslist/')
        return render(request, 'new_order.html', {'form': form})


# Rendering Order List page
def orders_list(request):
    #retrieving order list from database by author
    context = {'orders_list':NewOrderModel.objects.filter(author=request.user)}
    return render(request, 'orders_list.html', context)


# Delete Order from database
def delete_order(request, id):
    order = NewOrderModel.objects.get(pk=id)
    order.delete()
    return redirect('/orderslist/')


# Rendering Contact us page
def contact(request):
    # if the method is GET it will render the contact form
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        ## checks if the form is valid and save to database
        if form.is_valid():
            form.save()
        return redirect('home')


# Rendering About Us page
def about(request):
    return render(request, 'about.html')
