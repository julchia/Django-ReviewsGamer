# Generated by Django 2.1.7 on 2020-09-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsapp', '0004_auto_20200909_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='plataform',
            field=models.CharField(choices=[('Multiplataforma', 'MULTIPLATAFORMA'), ('PC', 'PC'), ('Playstation', 'PLAYSTATION'), ('Xbox', 'XBOX'), ('Nintendo', 'NINTENDO'), ('Sega', 'SEGA'), ('Game Boy', 'GAME BOY'), ('Mobil', 'MOBIL')], default='Multi', max_length=30),
        ),
    ]
