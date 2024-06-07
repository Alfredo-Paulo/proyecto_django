from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {'public_flans': public_flans}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {'private_flans': private_flans}
    return render(request, 'welcome.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def login(request):
    return render(request, 'login.html')
