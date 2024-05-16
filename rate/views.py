from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
from .models import *

def index(request):
    context = {}
    return render (request, "rate/index.html", context)

def about(request):
    context = {}
    return render (request, "rate/about.html", context)

def fees(request):
    context = {}
    return render (request, "rate/fees.html", context)


def bitcoin_leverage(request):
    context = {}
    return render (request, "rate/bitcoin_leverage.html", context)

def all_trading(request):
    context = {}
    return render (request, "rate/all_trading.html", context)

@login_required (login_url = "login")
def customer(request):
    context = {}
    return render (request, "rate/customer.html", context)

@login_required (login_url = "login")
def deposit_history(request):
    context = {}
    return render (request, "rate/deposit_history.html", context)

@login_required (login_url = "login")
def deposit(request):
    context = {}
    return render (request, "rate/deposit.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('customer')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('customer')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "rate/login.html", context)

def long_short_trade(request):
    context = {}
    return render (request, "rate/long_short_trade.html", context)

def partners(request):
    context = {}
    return render (request, "rate/partners.html", context)

def platform(request):
    context = {}
    return render (request, "rate/platform.html", context)

@login_required (login_url = "login")
def referals(request):
    context = {}
    return render (request, "rate/referals.html", context)

def security(request):
    context = {}
    return render (request, "rate/security.html", context)

@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('details')

    context = {'form': form}
    return render (request, "rate/register.html", context)

def terms(request):
    context = {}
    return render (request, "rate/terms.html", context)

@login_required (login_url = "login")
def withdraw(request):
    context = {}
    return render (request, "rate/withdraw.html", context)

@login_required (login_url = "login")
def pin(request):
    context = {}
    return render (request, "rate/pin.html", context)


@login_required (login_url = "login")
def details(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "rate/details.html", context)

@login_required (login_url = "login")
def processing(request):
    context = {}
    return render (request, "rate/processing.html", context)