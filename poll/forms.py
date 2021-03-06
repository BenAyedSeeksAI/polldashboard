from django.forms import ModelForm
from .models import poll, choice

class pollForm(ModelForm):
    class Meta:
        model = poll
        fields = ['question']