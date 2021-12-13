from django.db import models


# Create your models here.

class Host(models.Model):
    ip = models.CharField(max_length=15)
    cpu_name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=20, default='')
    cpu_base_clock = models.CharField(max_length=10, default='')
    disk = models.CharField(max_length=100)
    hostname = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    bios_version = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    memory_detail = models.CharField(max_length=100)
    is_actve = models.BooleanField(default=True)
    lab_name = models.CharField(max_length=10, default='')
    rack_name = models.CharField(max_length=30, default='')
    rack_position = models.CharField(max_length=20, default='')

    def __str__(self):
        return '%s object ["hostname":%s]' % (self.__class__.__name__, self.hostname)
    

    