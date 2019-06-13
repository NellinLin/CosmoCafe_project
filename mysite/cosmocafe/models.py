from django.db import models
from django.urls import reverse

def upload_location(instance,filename):
    return "galery_photo/%s" %(filename)


class Post(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    content = models.TextField()
    image = models.FileField(upload_to = "post_photo/", null=True,blank=True)

    def __str__(self):
        return self.name

    def get_adsolute_url(self):
        return reverse("post:detail",kwargs={"id":self.id})

class Galery(models.Model):
    image = models.FileField(upload_to = upload_location, null=True, blank=True)

#____________________________________________


class Cake(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=255)
    text = models.TextField(verbose_name='Текст описания')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    image = models.FileField(upload_to="cake_photo/", null=True, blank=True)

    def __str__(self):
        return ' Кекс {}, Цена {}'.format(self.title, self.price)


class Cupcake(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=255)
    text = models.TextField(verbose_name='Текст описания')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    image = models.FileField(upload_to="cupcake_photo/", null=True, blank=True)

    def __str__(self):
        return ' Пироженое {}, Цена {}'.format(self.title, self.price)


class Macaroon(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=255)
    text = models.TextField(verbose_name='Текст описания')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    image = models.FileField(upload_to="Macaroon_photo/", null=True, blank=True)

    def __str__(self):
        return ' Макарун {}, Цена {}'.format(self.title, self.price)

class Drink(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=255)
    text = models.TextField(verbose_name='Текст описания')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    image = models.FileField(upload_to="Drink/", null=True, blank=True)

    def __str__(self):
        return ' Напиток {}, Цена {}'.format(self.title, self.price)