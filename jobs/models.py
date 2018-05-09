from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 200, null=True)
    languages = models.CharField(max_length = 200, null=True)
    summary = models.TextField()

class Description(models.Model):
    bodyText = models.TextField(null=True)

    def summary(self):
        return self.bodyText

