from django.db import models
from django.contrib.auth.models import User,auth

# class Profile(models.Model):

#     skill=models.ForeignKey(Skill,on_delete=models.CASCADE)
#     work_link=models.ForeignKey(WorkLink,on_delete=models.CASCADE)
#     dp=models.ImageField(upload_to="pics", height_field=None, width_field=None, max_length=None)
#     username=User.username
#     name=str(User.first_name)+str(User.last_name)
#     email=User.email
#     phone=models.BigIntegerField(default="")
#     profession=models.CharField(default="", max_length=50)
#     experience=models.CharField(default="", max_length=50)
#     rate=models.IntegerField(default="")
#     eng_level=models.CharField(default="",max_length=10)
#     completedProjectNo=models.IntegerField(default="")
#     availability=models.IntegerField(default="")
#     bio=models.IntegerField(default="")
#     def __str__(self):
#         return self.username


