from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)
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