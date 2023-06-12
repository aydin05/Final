from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import SalesInvoice, Article, Customer


def home(request):
    sales_invoices = SalesInvoice.objects.all()
    articles = Article.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please try Again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'sales_invoices': sales_invoices, 'articles': articles})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def sales_invoices(request, pk):
    if request.user.is_authenticated:
        sales_invoices = SalesInvoice.objects.get(id=pk)
        return render(request, 'sales_invoice.html', {'sales_invoices': sales_invoices})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')
