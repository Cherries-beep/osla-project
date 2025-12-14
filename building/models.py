from django.core.exceptions import ValidationError
from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255, blank=False)
    entity = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    organizations = models.ManyToManyField(
        "Organization", related_name="buildings", blank=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Объект строительства"
        verbose_name_plural = "Объекты строительства"


class Organization(models.Model):
    """Модель организации

    Args:
        name (str): Название организации
        employees_count (int): Количество сотрудников
        external_id (str): Уникальный идентификатор
        created_at (datetime): Дата создания записи
        updated_at (datetime): Дата обновления записи
    """
    name = models.CharField(max_length=255)
    employees_count = models.PositiveIntegerField()
    external_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Класс для метаданных модели"""

        ordering = "-created_at"
        verbose_name = "Организация"  # админка
        verbose_name_plural = "Организации"  # админка

    def clean(self):
        """Валидация данных перед сохранением.

        Return:
            ValidationError: Если данные некорректны
        """
        errors = {}

        if len(str(self.name).strip()) < 2:
            errors["name"] = "Название должно содержать минимум 2 символа."

        if self.employees_count > 100000:
            errors['employees_count'] = ('Количество сотрудников не может превышать 100000.')

        if self.employees_count < 1:
            errors['employees_count'] = ('Количество сотрудников должно быть положительным числом.')

        if not str(self.external_id).strip():
            errors["external_id"] = "External ID не может быть пустым."

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        """Сохраняет объект после валидации"""
        self.full_clean()  # встроеннная проверка типов, очистка и проверка уникальности
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.external_id})"