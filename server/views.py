from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .utils import *
from .models import *


# Create your views here.

def show_all_host(request):
    host_list = Host.objects.filter(is_active=1)
    return render(request, 'host_list.html', locals())

def show_dashboard(request):
    labs = {}
    # print(request.path)
    return render(request, 'dashboard.html', locals())

def add_host(request):
    if request.method == 'POST':
        #判断ip是否为空
        if request.POST.get('add_host_ip', None):
            # is_ip_exists()
            # 当值为false时，则表示数据库中未添加当前ip
            if not Host.objects.filter(Q(ip=request.POST.get('add_host_ip')) & Q(is_active=1)).exists():
                # print("No records")
                new_host = generate_host_data(Host(), 
                    request.POST.get('add_host_ip'),
                    request.POST.get('add_host_port'),
                    request.POST.get('add_host_username'),
                    request.POST.get('add_host_password'))
                new_host.owner = request.POST.get('add_host_owner', None)
                new_host.lab_name = request.POST.get('add_host_which_lab', None)
                new_host.save()
                return redirect(show_all_host)
    return redirect('www.baidu.com')

# get all host info by host.id
def show_host_detail(request):
    # print(request.GET.get('id'))
    host_qs = Host.objects.filter(Q(id=request.GET.get('id')) & Q(is_active=1))
    host = host_qs[0]
    return render(request, 'host_detail.html', locals())

def update_host(request):
    host_list = Host.objects.filter(Q(is_active=1))
    for host in host_list:
        host = generate_host_data(host, host.ip, host.port, host.username, host.password)
        host.save()
        # print(host.ip)
    return redirect(show_all_host)