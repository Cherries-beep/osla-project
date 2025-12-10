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

    created_at = models.DateTimeField(auto_now_add=True)  #  для consistency
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


    def clean(self):
        """Валидация данных перед сохранением"""
        errors = {}
        
        if len(str(self.name).strip()) < 2:
            errors['name'] = _('Название должно содержать минимум 2 символа.')
        
        if self.employees_count > 100000:
            errors['employees_count'] = _('Количество сотрудников не может превышать 100000.')
        if self.employees_count < 1:
            errors['employees_count'] = _('Количество сотрудников должно быть положительным числом.')

        if not str(self.external_id).strip():
            errors['external_id'] = _('External ID не может быть пустым.')
    
        if errors:
            raise ValidationError(errors)
    
    def save(self, *args, **kwargs):
        """Автоматически вызывает валидацию перед сохранением"""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.external_id})"