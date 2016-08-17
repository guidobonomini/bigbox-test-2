from django.db import models

class UserProfile(models.Model):

    GENDERS = (('Female', 'Mujer'), ('Male', 'Hombre'))
    #Added max_length since it's a requirement for Django 1.9
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name="sexo")
    name = models.CharField(max_length=100, verbose_name="nombre")

class Order(models.Model):

    #Change original STATES object since Django 1.9 uses Tupples for choices
    STATES = (('INTENDED', 'Preorden'),

            ('IN_PROGRESS', 'En Progreso'),

            ('CANCELLED', 'Cancelada'),

            ('SUCCESSFUL', 'Exitosa'))

    state = models.CharField(max_length=11, choices=STATES, default='INTENDED', verbose_name="estado")

    user = models.ForeignKey(UserProfile, verbose_name="usuario")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")


class Laptop(models.Model):

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="precio")

    color = models.CharField(max_length=20)

    weight = models.IntegerField(verbose_name="peso")

    processor = models.CharField(max_length=30, verbose_name="procesador")

    ram = models.CharField(max_length=10)

    order = models.ForeignKey(Order, verbose_name="orden", related_name='laptop')



class Cámara(models.Model):

    CAMERA_TYPES = (('Digital', 'Digital'),('Reflex', 'Reflex'))

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="precio")

    color = models.CharField(max_length=20)

    weight = models.IntegerField(verbose_name="peso")

    cameraType = models.CharField(max_length=7, choices=CAMERA_TYPES, default='Digital', verbose_name="tiposCámara")

    megapixels = models.IntegerField()

    order = models.ForeignKey(Order, verbose_name="orden", related_name='cámara')
    

class Minicomponente(models.Model):

    USB = (('Yes','Sí'),('No', 'No'))

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="precio")

    color = models.CharField(max_length=20)

    weight = models.IntegerField(verbose_name="peso")

    power = models.IntegerField(verbose_name="potencia")

    usb = models.CharField(max_length=30, choices=USB, default='Yes')

    order = models.ForeignKey(Order, verbose_name="orden", related_name='minicomponente')
