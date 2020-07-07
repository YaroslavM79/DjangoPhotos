from django.db import models
from django.urls import reverse


# Create your models here.
class picture_blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Publish date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def get_absolute_url(self):
        return reverse('view_pictures', kwargs={'pk': self.pk})

    def __str__(self):
        return f'created_at = {self.created_at}'

    class Meta:
        verbose_name='Picture Blog'
        verbose_name_plural = 'Pictures blog'
        ordering = ['-created_at']

