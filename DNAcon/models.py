from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    group = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


from django.core.validators import FileExtensionValidator


class StudyMaterial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    video = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )


    def __str__(self):
        return self.title
