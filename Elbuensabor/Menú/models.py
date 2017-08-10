from django.db import models

# Create your models here.

class employe(models.Model1):
    generes=(
            ('f', 'female'),
            ('M', 'Male')
)
    
    lastname=models.Charfield(max_leght=50,help_text='Ingrese el apellido del empleado')
    age=models.Charfield(max_legth=20,help_text='Ingrese la edad del empleado')
    date of birthday=models.datefield(help_text='Ingrese la fecha de nacimiento del empleado')
    category=  models.CharField(max_length=1, help_text= 'Seleccione el sexo del empleado' choices=generes)

class restaurant(models.Model):
    categories =(
    ('B','Breakfast'),
    ('L','Lunch'),
    ('Dn','Dinner'),
    ('Dr','Drinks'),
    ('D','Dessert')
    )
    title=models.CharField(max_lenght=60,help_text='Ingrese la descripcion del platillo:')
    typerestaurant=models.Charfield(max_lenght=50,held_text='Que tipo de platillo desea:')
    price=models.Charfield(max_lenght=50,held_text='El precio del platillo es:')
    time=models.Charfield(max_lenght=50,held_text='El tiempo del platillo es:')
    category=models.Charfield(max_lenght=1,help_text='Seleccione su platillo:' choices=categories)

class stock (models.Model):
    product=models.Foreignkey(producto)
    stock=models.Integerfield(held_text='Ingrese la cantidad de platillos:')
