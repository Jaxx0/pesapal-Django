import urllib.request

from . import pesapal_processor3


def post_transaction(Reference, FirstName, LastName, Email, PhoneNumber, Description, Amount, Type):
    pesapal_processor3.consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
    pesapal_processor3.consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    pesapal_processor3.testing = False

    post_params = {
        'oauth_callback': 'http://32c65eea.ngrok.io/payment/oauth_callback/'
    }

    request_data = {
        'Amount': str(Amount),
        'Description': Description,
        'Type': 'MERCHANT',
        'Reference': Reference,
        'PhoneNumber': str(PhoneNumber),
        'Email': Email,
        'FirstName': FirstName,
        'LastName': LastName
    }

    url = pesapal_processor3.postDirectOrder(post_params, request_data)

    return url


def get_detailed_order_status(merchant_reference, transaction_tracking_id):
    pesapal_processor3.consumer_key = 'nRZXsEDVT2uMetIZxnusQPOA4zHyBtlV'
    pesapal_processor3.consumer_secret = 'UzKwzyN9GbXgSNC8HKcMHrJusME='

    post_params = {
        'pesapal_merchant_reference': merchant_reference,
        'pesapal_transaction_tracking_id': transaction_tracking_id
    }
    url = pesapal_processor3.queryPaymentDetails(post_params)
    response = urllib.request.urlopen(url)

    return response.read()


def get_payment_status(merchant_reference, transaction_tracking_id):
    pesapal_processor3.consumer_key = 'nRZXsEDVT2uMetIZxnusQPOA4zHyBtlV'
    pesapal_processor3.consumer_secret = 'UzKwzyN9GbXgSNC8HKcMHrJusME='

    post_params = {
        'pesapal_merchant_reference': merchant_reference,
        'pesapal_transaction_tracking_id': transaction_tracking_id
    }
    url = pesapal_processor3.queryPaymentStatus(post_params)
    response = urllib.request.urlopen(url)

    return response.read()
