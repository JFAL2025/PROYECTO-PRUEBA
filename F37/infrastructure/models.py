# Infrastructure layer: Contains Django models.
# IMPORTANT: Move your model definitions here from the default models.py.
from django.db import models

class ExampleModel(models.Model):
    # TODO: define your model fields
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
