from django.db import models
from django_resized import ResizedImageField
from tinymce.models import HTMLField

class categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class getpost(models.Model):
    category = models.ForeignKey(categories, related_name='categorypost', on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    body = HTMLField()
    photo = ResizedImageField(size=[851, 315], upload_to="gallery", blank=True, null=True)

    def __str__(self):
        return self.title
