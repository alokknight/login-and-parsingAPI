from django.contrib import admin

# Register your models here.
from .models import  Form_fields,Csv
admin.site.register(Form_fields)
admin.site.register(Csv)

