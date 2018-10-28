from djongo import models

class Memo(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    tags = models.ListField()