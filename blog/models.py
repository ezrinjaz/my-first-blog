# These import bits from other files
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # Class indicates we are defining an object. Post is the name of our model. models.Model means the Post is a Django Model, so Django knows it should be saved in the Database. 
    # Define properties below. Django documentation: https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # Methods often return something. 