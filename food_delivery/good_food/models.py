from django.db import models


class BeFit(models.Model):
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
