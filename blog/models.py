from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        pos = self.body.find(".", 100)
        if pos == -1:
            pos = len(self.body)
        return self.body[:(pos+1)]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
