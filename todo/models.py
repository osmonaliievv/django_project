from django.db import models
from library.models import Books
from django.views import generic


class TodoModel(models.Model):
    ITEM_CONDITION_CHOICES = (
        ("в налиции", "в налиции"),
        ("нет в наличии", "нет в наличии")
    )
    status = models.TextField(choices=ITEM_CONDITION_CHOICES)
    choise_book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.choise_book.title} {self.status}'
