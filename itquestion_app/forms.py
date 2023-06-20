from .models import RequestModel
from django.forms import ModelForm


class RequestForm(ModelForm):
    class Meta:
        model = RequestModel
        fields = ["Requestor", "Beneficiary", "AssetNumber", "Category", "Comment", ]
