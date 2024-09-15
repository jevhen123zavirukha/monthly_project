from django.db import models


class Technicians(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='technicians')
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Technician'
        verbose_name_plural = 'Technicians'
        ordering = ('sort', )

    def __str__(self):
        return self.name
