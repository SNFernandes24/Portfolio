from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def date_less_detail(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
