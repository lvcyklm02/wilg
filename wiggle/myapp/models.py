from django.db import models


class Exec(models.Model):
    name = models.CharField(max_length=100)
    position = models.TextField()
    classyear = models.PositiveIntegerField()
    description = models.TextField(default="wilglette")

    def __str__(self):
        return self.name
