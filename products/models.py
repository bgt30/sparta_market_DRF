from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("최대 파일 크기는 %sMB 입니다" % str(megabyte_limit))

    image = models.ImageField(
        upload_to='products/',
        validators=[validate_image],
        help_text='최대 5MB'
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products', blank=True)

    class Meta:
        ordering = ['-created_at'] 

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs) 