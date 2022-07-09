from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mascotitas/home.html')

def contacto(request):
    return render(request, 'mascotitas/contacto.html')