# Generated by Django 3.2.5 on 2021-07-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BibliotekaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazka',
            name='uzytkownik',
            field=models.CharField(default='', max_length=50),
        ),
    ]
