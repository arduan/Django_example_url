from django.db import models

class Bd(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True, blank=True)
    data_public = models.DateTimeField(auto_now_add=True, db_index=True)


