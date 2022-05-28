from django.contrib import admin
from art.models import HomeGallery, Gallery, Paintings, Contact, Art_Work, Wildlife, Street_Art, Everyday_Life,History, Nature, Art_Gallery

# Register your models here.
@admin.register(HomeGallery)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img', 'title')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')


@admin.register(Paintings)
class PaintingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(Art_Work)
class Art_Work_Admin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(Wildlife)
class WildlifeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')


@admin.register(Everyday_Life)
class Everyday_LifeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(Art_Gallery)
class Art_Gallery_Admin(admin.ModelAdmin):
    list_display = ('id', 'gallery_img')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email')