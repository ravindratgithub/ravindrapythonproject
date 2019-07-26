from django.db import models

class Admin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    contactno = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    categoryid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Categories(models.Model):
    categoriesID=models.IntegerField(primary_key=True)
    categoriesNAME=models.CharField(max_length=50)
    description=models.CharField(max_length=100)


class Product(models.Model):
    productId=models.IntegerField(primary_key=True)
    productName=models.CharField(max_length=30)
    productCategory=models.CharField(max_length=30)
    productDescription=models.CharField(max_length=100)
    owner=models.CharField(max_length=30)
    phoneNo=models.IntegerField()
    emailId=models.EmailField(max_length=100)
    postDate=models.DateField()
    cost=models.DecimalField(max_digits=20,decimal_places=2)
    image=models.FileField(upload_to="media/image",default=False)

class Userlogn(models.Model):
    userId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email_Id=models.EmailField(max_length=100)
    phone_No=models.IntegerField()
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=150)