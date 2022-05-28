from django.db import models

# Create your models here.
class HomeGallery(models.Model):
    gallery_img = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Paintings(models.Model):
    gallery_img = models.ImageField(upload_to='media')

class Art_Work(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Wildlife(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Street_Art(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Everyday_Life(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class History(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Nature(models.Model):
    gallery_img = models.ImageField(upload_to='media')


class Art_Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='media')

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    msg = models.TextField(max_length=70)

    def __str__(self):
        return self.name