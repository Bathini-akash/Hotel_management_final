from django.db import models
class Member(models.Model):
    mid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    memail=models.CharField(max_length=50,unique=True)
    levelchoice=(('B','Basic'),('S','Silver'),('G','Gold'),('P','Platinum'),)  
    level=models.CharField(max_length=1,choices=levelchoice)
    profile_pic=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,blank=True)
class MemberPhone(models.Model):
    mid=models.ForeignKey(Member,on_delete=models.CASCADE)
    phone1=models.CharField(max_length=10) 
    phone2=models.CharField(max_length=10)
class MemberPass(models.Model):
    mid=models.ForeignKey(Member,on_delete=models.CASCADE)  
    password=models.CharField(max_length=5)
class Guest(models.Model):
    gid=models.AutoField(primary_key=True) 
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    gemail=models.CharField(max_length=50)
    phone1=models.CharField(max_length=10)
    phone2=models.CharField(max_length=10)
    mid=models.ForeignKey(Member,on_delete=models.CASCADE,null=True,blank=True)

