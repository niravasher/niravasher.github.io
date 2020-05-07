from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default='')
    links = models.URLField(max_length=200, null=True, blank=True)
    files = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)

    def __str__(self):
        return self.title
