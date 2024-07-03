from django.db import models
from django.utils import timezone


class Baner(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    background_img = models.ImageField()

    def __str__(self):
        return self.title


class House(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    detail = models.TextField()

    def __str__(self):
        return self.name


class RoomImg(models.Model):
    img = models.ImageField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.house.name


class Service(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_watch = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.f_name}, {self.l_name}"


class Info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.phone
    


class Agent(models.Model):
    A_name=models.CharField(max_length=255)
    text=models.TextField()
    img=models.ImageField()


class Home_imgs(models.Model):
    img = models.ImageField()
    money=models.IntegerField(default=24450)
    text=models.TextField()
    body = models.TextField()

class  Contct_us(models.Model):
    Adress=models.TextField()
    Phone=models.CharField(max_length=13)
    Email=models.EmailField()