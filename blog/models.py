from django.db import models

# Create your models here.


class Blog(models.Model):
    title =  models.CharField(max_length=50)
    body = models.TextField()
    datePublished = models.DateField()
    image = models.ImageField(upload_to='images/')


    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.datePublished.strftime('%b %e %Y')

    def __str__(self):
        return self.title
