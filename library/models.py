from django.db import models

# Create your models here.

class Book(models.Model):
    class GenderChoice(models.TextChoices):
        Fantasia = 'Fantasia'
        Romance = 'Romance'
        Drama = 'Drama'
        Novela= 'Novela'
        Aventura = 'Aventura' 
        Ficcao_Cientifica = 'Ficção Científica'
        Terror = 'Terror'
    
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    isbn = models.DecimalField(decimal_places=2, max_digits=18)
    image = models.ImageField(blank = True)
    price = models.DecimalField(default=29.90,decimal_places=2, max_digits=18)
    gender = models.CharField(
        max_length=50, choices=GenderChoice.choices
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
