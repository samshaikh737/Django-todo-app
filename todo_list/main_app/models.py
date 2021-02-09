from django.db import models


class TodoData(models.Model):
    input_text = models.CharField(max_length=200)
