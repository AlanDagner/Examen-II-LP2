from django.db import models

# Create your models here.
class Socio(models.Model):

    codigo=models.IntegerField()
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=10)
    apellido_materno=models.CharField(max_length=10)
    sede=models.CharField(max_length=10)

    class Meta:
        verbose_name = ("Socio")
        verbose_name_plural = ("Socios")

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    socio=models.ForeignKey("Socio", on_delete=models.CASCADE)
    n_reunion=models.CharField(max_length=10, null=True)
    fecha=models.CharField(max_length=10, null=True)
    llego_a_tiempo=models.CharField(max_length=2, null=True)

    class Meta:
        verbose_name = ("Asistencia")
        verbose_name_plural = ("Asistencias")

    def __str__(self):
        return self.n_reunion

