from django.db import models

class textutils(models.Model):
    text = models.CharField(max_length=50)
    extra_space = models.BooleanField(default=False)
    count = models.BooleanField(default=False)
    uppercase = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text