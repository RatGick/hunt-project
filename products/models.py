from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(default='')
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e %Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:200]
