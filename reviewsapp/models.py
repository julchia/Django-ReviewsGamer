from django.db import models
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reviews(models.Model):
    PLATAFORM_CHOICES = (
        ('Multiplataforma', 'MULTIPLATAFORMA'),
        ('PC', 'PC'),
        ('Playstation', 'PLAYSTATION'),
        ('Xbox', 'XBOX'),
        ('Nintendo', 'NINTENDO'),
        ('Sega', 'SEGA'),
        ('Game Boy', 'GAME BOY'),
        ('Mobil', 'MOBIL'),
    )

    GENRE = (
        ('Acción', 'ACCION'),
        ('Plataformas', 'PLATAFORMAS'),
        ('FPS', 'FPS'),
        ('Deporte', 'DEPORTE'),
        ('Lucha', 'LUCHA'),
        ('Carrera', 'CARRERA'),
        ('Terror', 'TERROR'),
        ('Estrategia', 'ESTRATEGIA'),
        ('Educativo', 'EDUCATIVO'),
        ('RPG', 'RPG'),
        ('MMORPG', 'MMORPG'),
        ('Sandbox', 'SANDBOX'),
        ('Battle Royale', 'BATTLE ROYALE')
    )

    SCORE = (
        ('Obra maestra', 'OBRA MAESTRA'),
        ('Excelente', 'EXCELENTE'),
        ('Muy bueno', 'MUY BUENO'),
        ('Bueno', 'BUENO'),
        ('Regular', 'REGULAR'),
        ('Malo', 'MALO'),
        ('Muy malo', 'MUY MALO'),
        ('Pésimo', 'PESIMO'),
        ('No lo compres', 'NO LO COMPRES'),
    )

    STATUS = (
        ('Aprobado', 'APROBADO'),
        ('Revisar', 'REVISAR'),
        ('No aprobado', 'NO APROBADO')
    )

    game_name = models.CharField(max_length=30)
    plataform = models.CharField(max_length=30, choices=PLATAFORM_CHOICES, default='Multi')
    genre = models.CharField(max_length=30, choices=GENRE, default='Acción')
    release_year = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(3000)], default=2000)
    review = models.TextField()
    score = models.CharField(max_length=30, choices=SCORE, default='Regular')
    cover = models.ImageField(upload_to='reviewsapp_covers')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS, default='Revisar')

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.game_name