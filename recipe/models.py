from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'Граммы'),
        ('kg', 'Килограммы'),
        ('ml', 'Миллилитры'),
        ('l', 'Литры'),
        ('pcs', 'Штуки'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название ингредиента")
    quantity = models.FloatField(verbose_name="Количество")
    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        verbose_name="Единица измерения"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name="Рецепт"
    )

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.get_unit_display()})"
