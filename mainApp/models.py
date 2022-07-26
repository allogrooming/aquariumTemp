from distutils.text_file import TextFile
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

class MemberTest(models.Model):
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=20)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1)
    member_dob = models.DateField()
    member_join_date = models.DateTimeField(auto_now=True)
    member_pic = models.TextField()

class user(models.Model):
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=20)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1)
    member_dob = models.DateField()
    member_join_date = models.DateTimeField(auto_now=True)
    member_pic = models.TextField()