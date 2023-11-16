from django.shortcuts import render

# Rendering home page
def home(request):
    return render(request, 'base.html')