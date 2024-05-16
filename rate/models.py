from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


kyc = (
    ('$', 'US Dollar $'),
    ('£ ', 'Pound Sterling £'),
    ('€', 'Euro €'),
    )


class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)
    currency = models.CharField (max_length=24, choices=kyc, default='$')

    def __str__(self):
        return str(self.name)

class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    active_deposit = models.CharField (max_length = 200, null = True, default='0')
    main_deposit = models.CharField (max_length = 200, null = True, default='0')
    added_bonus = models.CharField (max_length = 200, null = True, default='0')
    withdraw_funds = models.CharField (max_length=24, null = True, default='0.00')

    def __str__(self):
        return str(self.name)

class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    wallet = models.CharField (max_length = 200, null = True, default='0')

    def __str__(self):
        return str(self.name)


choices = [
    ('sweetAlert', 'sweetAlert'),
    ('paid',"paid"),
]
    
STATUS = (
    ('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('KYC has not been uploaded kindly fill in your details on your kyc data table', 'KYC has not been uploaded kindly fill in your details on your kyc data table'),
    )

kyc = (
    ('swal-2', 'swal-2'),
    ('swal-4', 'swal-4'),
    )

class Alert (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    alert = models.CharField (max_length=24, choices=choices, default='sweetAlert')
    status = models.CharField (max_length=200, null=True, choices=STATUS, default='You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.')
    kyc = models.CharField (max_length=24, choices=kyc, default='#swal-4')

    def __str__(self):
        return str(self.name)


class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


statu = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    )

class Transaction (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)
    amount = models.CharField (max_length = 200, null = True)
    status = models.CharField (max_length=200, null=True, choices=statu, default='Pending')


    def __str__(self):
        return str(self.name)