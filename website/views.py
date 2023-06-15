from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddInvoiceForm, AddArticleForm
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
        sales_invoice = SalesInvoice.objects.get(id=pk)
        articles = sales_invoice.articles.all()
        return render(request, 'sales_invoice.html', {'sales_invoice': sales_invoice, 'articles': articles})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')


def delete_invoice(request, pk):
    if request.user.is_authenticated:
        delete_it = SalesInvoice.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Invoice has been removed!')
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')


def add_invoice(request):
    form = AddInvoiceForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_invoice = form.save()
                messages.success(request, "Invoice has been created!")
                return redirect('home')
        return render(request, 'add_invoice.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def update_invoice(request, pk):
    if request.user.is_authenticated:
        current_invoice = SalesInvoice.objects.get(id=pk)
        form = AddInvoiceForm(request.POST or None, instance=current_invoice)
        if form.is_valid():
            form.save()
            messages.success(request, "Invoice Has Been Updated!")
            return redirect('home')
        return render(request, 'update_invoice.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


def article(request, pk):
    if request.user.is_authenticated:
        articles = Article.objects.get(article_id=pk)
        return render(request, 'article.html', {'articles': articles})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')


def add_article(request):
    form = AddArticleForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_article = form.save()
                messages.success(request, "Article Has Been Created!")
                return redirect('home')
        return render(request, 'add_article.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def update_article(request, pk):
    if request.user.is_authenticated:
        current_article = Article.objects.get(article_id=pk)
        form = AddArticleForm(request.POST or None, instance=current_article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article Has Been Updated!")
            return redirect('home')
        return render(request, 'update_article.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')
