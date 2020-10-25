# Third party imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'uploads/user_{0}/{1}'.format(instance.title, filename)
class Post(models.Model):
    title = models.CharField(max_length=30, default='')
    summary = models.CharField(max_length=60, default='')
    body = models.CharField(max_length=300, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    document = models.FileField(default='placeholder.pdf', upload_to=user_directory_path)
    tags = models.CharField(default='', max_length=300, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
    
    def save(self, **kwargs):
        super().save()
