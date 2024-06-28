from django.db import models
from .interfaces import ESTADO_CHOICES, ESTADO_USO_CHOICES


class LaboratoriosModel(models.Model):
    nombre_laboratorio = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nombre del laboratorio"
    )

    class Meta:
        db_table = 'Laboratorios'
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'

    def __str__(self):
        return self.nombre_laboratorio


class MarcasModel(models.Model):
    nombre_marca = models.CharField(
        max_length=55,
        unique=True,
        verbose_name="Nombre de la marca"
    )

    class Meta:
        db_table = 'Marcas'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre_marca


class TipoActivosModel(models.Model):
    nombre_tipo = models.CharField(
        max_length=55,
        unique=True,
        verbose_name="Nombre del equipo"
    )

    class Meta:
        db_table = 'TipoActivos'
        verbose_name = 'Tipo de Activo'
        verbose_name_plural = 'Tipos de Activos'

    def __str__(self):
        return self.nombre_tipo


class ActivosModel(models.Model):
    codigo_activo = models.CharField(
        max_length=12,
        unique=True,
        verbose_name="Código del activo"
    )
    laboratorio = models.ForeignKey(
        LaboratoriosModel,
        on_delete=models.CASCADE
    )
    tipo = models.ForeignKey(TipoActivosModel, on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcasModel, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='OPERATIVO'
    )
    estado_uso = models.CharField(
        max_length=6,
        choices=ESTADO_USO_CHOICES,
        default='NUEVO'
    )
    observacion = models.TextField()
    imagen = models.ImageField(upload_to='activos/', blank=True, null=True)

    class Meta:
        db_table = 'Activos'
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'

    def __str__(self):
        return f"{self.codigo_activo} - {self.laboratorio}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()
