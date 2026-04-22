from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='categorias/',null=True,blank=True)
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)

    def __str__(self):
        return self.nombre  


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)  # 👈 más flexible
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # 🔥 clave para tienda
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)

    def __str__(self):
        return self.nombre