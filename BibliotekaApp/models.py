from django.db import models

# Create your models here.


class Ksiazka(models.Model):
    miekka = 'miekka'
    twarda = 'twarda'
    Typ_okladki = {
        (miekka, 'miekka'),
        (twarda, 'twarda'),
    }
    tytul = models.CharField(max_length=32, default='')
    autor = models.CharField(max_length=32, default='')
    typ_okladki = models.CharField(max_length=32, choices=Typ_okladki, default=miekka)
    wydawnictwo = models.CharField(max_length=35, default='')
    data_premiery = models.DateField(auto_now_add=True, auto_now=False, blank=False, null=True)
    data_publikacji = models.DateTimeField(default=None, null=True, blank=True)
    liczba_stron = models.IntegerField(default=1)
    uzytkownik = models.CharField(max_length=50, default='')
    zdjecie = models.ImageField(upload_to='okladki', default=None)
    is_active = models.IntegerField(default=1)#1 - active 0 - inactive
    def __str__(self):
        return self.tytul

