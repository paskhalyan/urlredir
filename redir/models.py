from django.db import models


class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    short_url = models.CharField(max_length=15, unique=True)
    created_date = models.DateTimeField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return str(self.url)
