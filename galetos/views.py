from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(None, "404.html", status=404)