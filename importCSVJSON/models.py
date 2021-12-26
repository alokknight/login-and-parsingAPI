from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded_time= models.DateTimeField(auto_now_add=True)
    file_type= models.CharField(max_length=100)
    encoding= models.CharField(max_length=100)
    delimiter= models.CharField(max_length=100)
    activated= models.BooleanField(default= True)
    def __str__(self):
        return f"file_id:[{self.file_name}]-{self.id}"

class Form_fields(models.Model):
    product_id= models.CharField(max_length=100,primary_key=True)
    Subcatogory= models.CharField(max_length=100)
    Title= models.CharField(max_length=100)
    price= models.PositiveIntegerField()
    Popularity =models.PositiveIntegerField()
    Description= models.TextField()
    Rating = models.PositiveIntegerField()
    UTM_Source= models.CharField(max_length=100)
    UTM_Medium= models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Title}"
