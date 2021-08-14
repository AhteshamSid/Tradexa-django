from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products', kwargs={'pk': self.pk})
