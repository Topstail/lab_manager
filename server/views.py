from django.shortcuts import render
from . import utils


# Create your views here.

def show_all_host(request):
    ip = '10.238.152.182'
    port = 22
    username = 'root'
    password = 'intel@123'
    host = utils.generate_host_data('10.238.152.182', 22, 'root', 'intel@123')
    print(host)
    print(host.hostname)
    return render(request, 'host_list.html', locals())

def show_dashboard(request):
    labs = {}
    print(request.path)
    return render(request, 'dashboard.html', locals())

