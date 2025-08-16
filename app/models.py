from django.db import models

# Create your models here.
class database(models.Model):
    name=models.CharField(max_length=50)
    url=models.ImageField(upload_to='images')
    uploaded_At=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    