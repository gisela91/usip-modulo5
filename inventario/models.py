from django.db import models
from django.conf import settings

class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.nombre

class ProductUnits(models.TextChoices):
	UNITS = 'u', 'Unidades'
	KG = 'kg', 'Unidades'

class Producto(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	description = models.TextField()
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	unidades = models.CharField(
		max_length=2,
		choices=ProductUnits.choices,
		default=ProductUnits.UNITS
		)
	disponible = models.BooleanField(blank=True, default=True)
	create = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

class EstadoOrden(models.TextChoices):
	NOPAGADO = 'nopagado', 'No pagado'
	PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
	total = models.IntegerField(default=0)
	fecha = models.DateField()
	vendedor =  models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="inventario_orden_vendedor"
		)
	estado = models.CharField(
		max_length=10,
		choices=EstadoOrden.choices,
		default=EstadoOrden.NOPAGADO
		)

class OrdenProducto(models.Model):
	orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	precio = models.DecimalField(decimal_places=2,max_digits=10)
	
