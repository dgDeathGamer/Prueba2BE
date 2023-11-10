from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    ELEGIR_TIPO = ( #para ver que tipo de cliente será, supongo que esto funcionará como un list o selectlist, no recuerdo como se llamaba...
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('empresarial', 'Empresarial'),
    )
    tipoCliente = models.CharField(max_length=20, choices=ELEGIR_TIPO)

    def __str__(self):
        return self.nombre