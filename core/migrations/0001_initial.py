# Generated by Django 4.0.5 on 2022-06-03 04:35

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now_add=True, verbose_name='Data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Altura')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
