from django import forms
from django.forms import ModelForm
from .models import Form_fields, Csv

class Form_fieldForm(forms.ModelForm):
	class Meta:
		model = Form_fields
		fields = '__all__'

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ("file_name",)