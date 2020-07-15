from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class PictureBlog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Publish date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    def get_absolute_url(self):
        return reverse('view_picture', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Photo'

    class Meta:
        verbose_name = 'Picture Blog'
        verbose_name_plural = 'Pictures blog'
        ordering = ['-created_at']

    def delete(self, *args, **kwargs):
        # Delete image file also
        storage, path = self.photo.storage, self.photo.path
        super(PictureBlog, self).delete(*args, **kwargs)
        storage.delete(path)
