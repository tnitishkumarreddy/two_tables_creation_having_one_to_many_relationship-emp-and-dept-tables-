from django.db import models
from django.db.models import SET_NULL
# Create your models here.

class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.DecimalField(max_digits=8,decimal_places=2)
    Comm=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    Hiredate=models.DateField(auto_now=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Mgr=models.ForeignKey('self',on_delete=SET_NULL,null=True,blank=True)