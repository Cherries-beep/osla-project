from django.db import models
from django.core.exceptions import ValidationError


class Building(models.Model):
    name = models.CharField(max_length=255, blank=False)
    entity = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    organizations = models.ManyToManyField("Organization", related_name="buildings", blank=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Объект строительства'
        verbose_name_plural = 'Объекты строительства'



class Organization(models.Model):
    name = models.CharField(max_length=255)
    employees_count = models.PositiveIntegerField()
    external_id = models.CharField(max_length=255, unique=True)

    def clean(self):

        if len(str(self.name).strip()) < 2:
            raise ValidationError({'name': 'Название должно содержать минимум 2 символа.'})

        if int(self.__dict__['employees_count']) > 100000:
            raise ValidationError({'employees_count': 'Количество сотрудников не может превышать 100000.'})