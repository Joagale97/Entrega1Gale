
from django.db import models

# Create your models here.
class Celulares (models.Model):
    marca= models.CharField( max_length=50)
    modelo= models.CharField( max_length=50)
    sistema_operativo= models.CharField( max_length=50)
    memoria_en_GB= models.PositiveBigIntegerField()
    compañia= models.CharField( max_length=50)
    cantidad= models.PositiveSmallIntegerField() 

    def __str__(self) :
        return f"Se solicitaron  {self.cantidad} celulares de marca {self.marca} para la compañia {self.compañia}"


