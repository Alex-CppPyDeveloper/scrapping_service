from django.db import models
from .dictionary import rus_in_eng

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населённого пункта',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Название населённого пункта'
        verbose_name_plural = 'Название населённых пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = rus_in_eng(str(self.name))
        super().save(*args, **kwargs)
        


class Language(models.Model):
    """docstring for Language"""
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name
