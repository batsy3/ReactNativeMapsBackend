from django.contrib.gis.db import models


class Area(models.Model):
    name = models.CharField(max_length=256,)
    description = models.CharField(max_length=256)
    polygonCoordinates = models.ForeignKey("PolygonList", null=True)

    def __str__(self):
        return self.name


class PolygonList(models.Model):
    pointA = models.ForeignKey("LatLang", null=True,)
    pointB = models.ForeignKey("LatLang", null=True,)
    pointC = models.ForeignKey("LatLang", null=True,)
    pointD = models.ForeignKey("LatLang", null=True,)


class LatLang(models.Model):
    latitude = models.PointField(
        "Location",
        geography=True,
        blank=True,
        null=True,
        srid=4326
    )
    longitude = models.PointField()
