from django.db import models


# Create your models here.

class Host(models.Model):
    ip = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    port = models.CharField(max_length=5)
    cpu_name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=20, default='')
    cpu_base_clock = models.CharField(max_length=10, default='')
    disk = models.CharField(max_length=500)
    hostname = models.CharField(max_length=20)
    os = models.CharField(max_length=40)
    bios_version = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    memory_detail = models.CharField(max_length=500, default='')
    is_active = models.BooleanField(default=True)
    lab_name = models.CharField(max_length=10, default='')
    rack_name = models.CharField(max_length=30, default='')
    rack_position = models.CharField(max_length=20, default='')

    def __str__(self):
        return ''' %s object ["ip				" : %s, "username		" : %s, "password		" : %s, "port			" : %s, "cpu_name		" : %s, "code_name		" : %s, "cpu_base_clock	" : %s, "disk			" : %s, "hostname		" : %s, "os				" : %s, "bios_version	" : %s, "owner			" : %s, "memory			" : %s, "memory_detail	" : %s, "is_actve		" : %s, "lab_name		" : %s, "rack_name		" : %s, "rack_position	" : %s, ] ''' % (self.__class__.__name__, self.ip, self.username, self.password, self.port, self.cpu_name, self.code_name, self.cpu_base_clock, self.disk, self.hostname, self.os, self.bios_version, self.owner, self.memory, self.memory_detail, self.is_active, self.lab_name, self.rack_name, self.rack_position)
