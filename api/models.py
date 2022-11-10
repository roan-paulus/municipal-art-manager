from django.db import models
from django_project.settings import BASE_DIR


class OverheidsGebouw(models.Model):  # MunicipalBuilding
    adres = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    stad = models.CharField(max_length=20)
    pand_code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Overheidsgebouwen"

    def __str__(self):
        return self.adres


# leave out a display location model, too hard to to keep up to date?
class Kamer(models.Model):  # Room
    verdieping = models.IntegerField()
    kamer_identificatie = models.CharField(max_length=30)  # room number, etc..
    gebouw = models.ForeignKey(OverheidsGebouw, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Kamers"

    def __str__(self):
        return f"{self.gebouw} {self.kamer_identificatie}"


class Artiest(models.Model):  # Artist
    naam = models.CharField(max_length=30)  # might be an alias or full name
    # kunstwerk_set for hidden artworks defined by ManyToManyField in Kunstwerk

    class Meta:
        verbose_name_plural = "Artiesten"

    def __str__(self):
        return self.naam


class Kunstwerk(models.Model):  # Artwork: the centerpiece of the database
    titel = models.CharField(max_length=30)
    artiesten = models.ManyToManyField(Artiest)
    beschrijving = models.TextField(blank=True)
    locatie = models.ForeignKey(Kamer, on_delete=models.PROTECT)
    # dimensions in centimeters (or to be determined)
    lengte = models.IntegerField(null=True)
    breedte = models.IntegerField(null=True)
    hoogte = models.IntegerField(null=True)

    # afbeelding = models.ImageField(upload_to="images")

    class Meta:
        verbose_name_plural = "Kunstwerken"

    def __str__(self):
        return self.titel

