from django.db import models


# Create your models here.
class Information(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.BigIntegerField()
    Passion = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

# username='admin'
# password=134
