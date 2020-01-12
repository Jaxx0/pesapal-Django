from django.forms import ModelForm
from . import models


class Payment(ModelForm):

    class Meta:
        model = models.Payment
        fields = ['country', 'first_name', 'last_name', 'email', 'phone', 'amount']