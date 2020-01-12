import json
import random
import string

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from . import pesapal_ops3

from . import forms


def home(request):
    return redirect(reverse('payment:pay'))


def payment(request):
    account_reference = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    if request.method == 'POST':
        form = forms.Payment(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.reference = account_reference
            payment.type = 'MERCHANT'
            payment.description = 'product purchased'
            Reference = payment.reference
            FirstName = payment.first_name
            LastName = payment.last_name
            Email = payment.email
            PhoneNumber = payment.phone
            Description = payment.description
            Amount = payment.amount
            Type = payment.type
            payment.save()
            iframe_src = pesapal_ops3.post_transaction(Reference, FirstName, LastName, Email, PhoneNumber, Description, Amount, Type)
            print(iframe_src)
            return render(request, 'payment/paynow.html', {'iframe_src': iframe_src})
    else:
        form = forms.Payment()
    return render(request, 'payment/index.html', {'form': form})


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        print(request.body)
        print('POST')
    else:
        params = request.GET
        print(params)
    merchant_reference = params['pesapal_merchant_reference']
    transaction_tracking_id = params['pesapal_transaction_tracking_id']
    print(merchant_reference)
    print(transaction_tracking_id)
    # status = pesapal_ops3.get_detailed_order_status(merchant_reference, transaction_tracking_id)
    status = pesapal_ops3.get_payment_status(merchant_reference, transaction_tracking_id).decode('utf-8')
    p_status = str(status).split('=')[1]

    return render(request, 'payment/status.html', {'status': p_status})
