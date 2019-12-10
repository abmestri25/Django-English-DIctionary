from django.db import models

class word(models.Model):
    text = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    

    def __str__(self):
        return self.text