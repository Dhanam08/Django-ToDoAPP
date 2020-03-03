from django.db import models
 
class todotable(models.Model):
    task=models.CharField(max_length=100)
    class Meta:
        db_table="todotbl"

