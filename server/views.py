from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from . import utils, models


# Create your views here.

def show_all_host(request):
    host_list = models.Host.objects.filter(is_active=1)
    return render(request, 'host_list.html', locals())

def show_dashboard(request):
    labs = {}
    print(request.path)
    return render(request, 'dashboard.html', locals())

def add_host(request):
    if request.method == 'POST':
        #判断ip是否为空
        if request.POST.get('add_host_ip', None):
            # is_ip_exists()
            # 当值为false时，则表示数据库中未添加当前ip
            if not models.Host.objects.filter(Q(ip=request.POST.get('add_host_ip')) & Q(is_active=1)).exists():
                print("No records")
                new_host = utils.generate_host_data(request.POST.get('add_host_ip'),
                    request.POST.get('add_host_port'),
                    request.POST.get('add_host_username'),
                    request.POST.get('add_host_password'))
                new_host.owner = request.POST.get('add_host_owner', None)
                new_host.lab_name = request.POST.get('add_host_which_lab', None)
                new_host.save()
                return redirect(show_all_host)
    return render(request, 'host_list.html', locals())