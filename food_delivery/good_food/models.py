from django.db import models


class BeFit(models.Model):
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Light(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Normal(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Strong(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class SuperStrong(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Super(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
