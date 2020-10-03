from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Product_tile(models.Model):
    tile_id = models.IntegerField(default = 0)
    tile_name = models.CharField(default="no name", max_length = 200)
    tile_image = CloudinaryField('avatar')
    tile_dimensions = models.CharField(default="no dimensions", max_length = 100)
    tile_application = models.CharField(default="no application", max_length = 100)
    tile_pattern = models.CharField(default="no pattern", max_length = 100)
    tile_color = models.CharField(default="no colour", max_length = 100)
    tile_texture = models.CharField(default="no texture", max_length = 100)

    def __str__(self):
        return f'{self.tile_id}'

class Home_page_images(models.Model):
    Image1 = CloudinaryField('avatar')
    Image2 = CloudinaryField('avatar')
    Image3 = CloudinaryField('avatar')

    def __str__(self):
        return f'Home page Image'