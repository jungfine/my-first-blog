from django.db import models
from django.utils import timezone


class Post(models.Model): #Post Class. First letter of class must be capital letter
    author = models.ForeignKey('auth.User') #'models' is for saving database,
    title = models.CharField(max_length=200) #limited text (Title)
    text = models.TextField() # unlimited text (content)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
