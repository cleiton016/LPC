# Generated by Django 2.1.7 on 2019-03-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128, verbose_name='título')),
                ('conteudo', models.TextField()),
                ('data_criacao', models.DateTimeField(verbose_name='Data da Criação')),
                ('data_publicacao', models.DateTimeField(verbose_name='Data da publicação')),
                ('publicado', models.BooleanField(verbose_name='Publicado')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]
