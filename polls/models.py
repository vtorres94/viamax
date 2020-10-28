from django.db import models
from django.urls import reverse

# Create your models here.
class Pagadores(models.Model):
    logo_base64=models.CharField(max_length=64)
    pagador=models.CharField(max_length=80)
    tipo_cambio=models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return 'Pagador : %s con tipo de cambio: %s' % (self.pagador, self.tipo_cambio)

    def get_absolute_url(self):
        return reverse('pagador_edit', kwargs={'pk': self.pk})
    