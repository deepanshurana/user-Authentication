from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields
    profilePic = models.ImageField(upload_to='profilePicDir', blank=True)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
