from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('all_trading/', views.all_trading, name = "all-trading"),
    path ('bitcoin_leverage/', views.bitcoin_leverage, name = "bitcoin-leverage"),
    path ('customer/', views.customer, name = "customer"),
    path ('fees/', views.fees, name = "fees"),
    path ('deposit_history/', views.deposit_history, name = "deposit-history"),
    path ('deposit/', views.deposit, name = "deposit"),
    path ('long_short_trade/', views.long_short_trade, name = "long-short-trade"),
    path ('partners/', views.partners, name = "partners"),
    path ('platform/', views.platform, name = "platform"),
    path ('referals/', views.referals, name = "referals"),
    path ('security/', views.security, name = "security"),
    path ('register/', views.register, name = "register"),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('terms/', views.terms, name = "terms"),
    path ('withdraw/', views.withdraw, name = "withdraw"),
    path ('details/', views.details, name = "details"),
    path ('pin/', views.pin, name = "pin"),
    path ('processing/', views.processing, name = "processing"),
 ]